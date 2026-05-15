from flask import Blueprint, request, jsonify
from src.services.publicationService import PublicationService
from src.config.database import SessionLocal
from src.utils.security import Security

publication_bp = Blueprint('publication', __name__, url_prefix='/api/publication')

@publication_bp.route('/', methods=['POST'])
def create_publication():
    data = request.get_json()
    payload = Security.verify_token(request.headers)
        
    if payload is not None:
        db = SessionLocal()
        
        gln = payload.get('gln')

        service = PublicationService(db)
        publication = service.createPublication(
            publicator = gln,
            gtin=data['gtin'],
            supplier=data['supplier'],
            subscriber=data['subscriber'],
        )

        db.close()
        
        if publication.get('Error'):
            return jsonify(publication), 400
        
        return jsonify({'id': publication['publication_id']}), 201
    else:
        return jsonify({'Message':'Unauthorized'}), 401
