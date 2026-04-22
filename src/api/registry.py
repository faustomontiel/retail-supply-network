from flask import Blueprint, request, jsonify
from src.services.registryService import RegistryService
from src.config.database import SessionLocal

registry_bp = Blueprint('registry', __name__, url_prefix='/registry')

@registry_bp.route('/create', methods=['POST'])
def create_registry():
    data = request.get_json()
    db = SessionLocal()

    service = RegistryService(db)
    registry = service.registryMessage(
        gtin=data['gtin'],
        name=data['name'],
        description=data['description']
    )

    db.close()
    return jsonify({'id': registry.id, 'gtin': registry.gtin}), 201
