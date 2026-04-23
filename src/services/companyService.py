from src.services.messageService import messageService, message
from sqlalchemy.orm import Session
from src.models.company import Company
import secrets

class CompanyService(messageService):
    def __init__(self, db: Session):
        super().__init__()
        self._db = db
        
    def createCompany(self, gln: str, name: str):
        password = secrets.token_urlsafe(12)

        company = Company(gln=gln, name=name, password=password)
        self._db.add(company)
        self._db.commit()
        self._db.refresh(company)
        return company        

class CompanyMessage(message):
    def __init__(self):
        super().__init__()
