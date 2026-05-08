from flask import Blueprint, request, jsonify
from src.services.companyService import CompanyService
from src.config.database import SessionLocal
from src.config.config import SUPER_USER_KEY
from src.utils.security import Security

company_bp = Blueprint('company', __name__, url_prefix='/api/company')

@company_bp.route('/', methods=['POST'])
def create_company():
    data = request.get_json()
    token = request.headers.get('Authorization', '').replace('Bearer ', '')

    if token != SUPER_USER_KEY:
        return jsonify({'Message':'Unauthorized'}), 401

    db = SessionLocal()

    service = CompanyService(db)
    company = service.createCompany(
        gln=data['gln'],
        name=data['name'],
        type=data['type']
    )
    db.close()

    if company.get('exist'):
        return jsonify(company), 409

    return jsonify(company), 201