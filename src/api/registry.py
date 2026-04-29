from flask import Blueprint, request, jsonify
from src.services.registryService import RegistryService
from src.config.database import SessionLocal
from src.utils.security import Security

registry_bp = Blueprint('registry', __name__, url_prefix='/api/registry')

@registry_bp.route('/', methods=['POST'])
def create_registry():
    data = request.get_json()
    payload = Security.verify_token(request.headers)
        
    if payload is not None:
        db = SessionLocal()
        
        gln = payload.get('gln')


        service = RegistryService(db)
        registry = service.registryMessage(
            gln=gln,
            gtin=data['gtin'],
            name=data['name'],
            description=data['description']
        )

        db.close()
        
        if registry.get('error'):
            return jsonify(registry), 400
        
        return jsonify({'id': registry['id'], 'gtin': registry['gtin']}), 201
    else:
        return jsonify({'Message':'Unauthorized'}), 401
