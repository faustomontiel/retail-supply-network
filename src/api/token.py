from flask import Blueprint, request, jsonify
from src.utils.security import Security

security_bp = Blueprint('security', __name__, url_prefix='/api/token')

@security_bp.route('/', methods=['POST'])
def generate_token():
    data = request.get_json()

    encode_token = Security.generate_token(
        gln=data['gln'],
        password=data['password']
    )

    if encode_token is None:
        return jsonify({'Error': f'Invalid credentials'})

    return jsonify({'success': True, 'token': encode_token})
