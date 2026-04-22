from flask import Blueprint, request, jsonify
from src.utils.security import Security

security_bp = Blueprint('security', __name__, url_prefix='/auth')

@security_bp.route('/token', methods=['POST'])
def generate_token():
    data = request.get_json()
    security = Security() 
    encode_token = security.generate_token()

    return jsonify({'success': True, 'token': encode_token})
