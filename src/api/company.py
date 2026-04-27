from flask import Blueprint, request, jsonify
from src.services.companyService import CompanyService
from src.config.database import SessionLocal

company_bp = Blueprint('company', __name__, url_prefix='/api/company')

@company_bp.route('/', methods=['POST'])
def create_company():
    data = request.get_json()
    db = SessionLocal()

    service = CompanyService(db)
    company = service.createCompany(
        gln=data['gln'],
        name=data['name']
    )

    db.close()

    if company.get('exist'):
        return jsonify(company), 409
    
    return jsonify(company), 201
