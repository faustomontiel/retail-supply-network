from datetime import datetime, timedelta, timezone
from flask import jsonify
from src.config.config import JWT_KEY
from src.services.companyService import CompanyService
from src.services.hashService import HashService
from src.config.database import SessionLocal
import jwt


class Security():
    @staticmethod
    def generate_token(gln: str, password: str):
        
        db = SessionLocal()
        companyService = CompanyService(db)    
        
        hashed_password = companyService.get_company_password(gln)
        
        if hashed_password is None:
            return None
        
        if not HashService.verify_password(password, hashed_password):
            return None

        now = datetime.now(timezone.utc)
        payload = {
            'gln': gln,
            'iat': int(now.timestamp()),
            'exp': int((now + timedelta(minutes=120)).timestamp())
        }
        return jwt.encode(payload, JWT_KEY, algorithm="HS256")

    @staticmethod
    def verify_token(headers):
        if 'Authorization' not in headers:
            return None 
        
        try:
            authorization = headers['Authorization']
            if not authorization.startswith('Bearer '):
                return None
            
            encoded_token = authorization.split(" ")[1]
            
            if len(encoded_token) == 0:
                return None
            
            payload = jwt.decode(encoded_token, JWT_KEY, algorithms=["HS256"])
            return payload 
        
        except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError, IndexError):
            return None
        except Exception:
            return None