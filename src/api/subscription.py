from flask import Blueprint, request, jsonify
from src.services.subscriptionService import SubscriptionService
from src.config.database import SessionLocal
from src.utils.security import Security

subscription_bp = Blueprint('subscription', __name__, url_prefix='/api/subscription')

@subscription_bp.route('/', methods=['POST'])
def create_subscription():
    data = request.get_json()
    payload = Security.verify_token(request.headers)
        
    if payload is not None:
        db = SessionLocal()
        
        gln = payload.get('gln')


        service = SubscriptionService(db)
        subscription = service.createSubscription(
            consultant=gln,
            supplier=data['supplier'],
            subscriber=data['subscriber'],
        )

        db.close()
        
        if subscription.get('error'):
            return jsonify(subscription), 400
        
        return jsonify({'id': subscription['subscription_id']}), 201
    else:
        return jsonify({'Message':'Unauthorized'}), 401
