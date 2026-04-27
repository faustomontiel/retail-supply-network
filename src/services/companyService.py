from src.services.messageService import messageService, message
from sqlalchemy.orm import Session
from src.models.company import Company
import secrets

class CompanyService(messageService):
    def __init__(self, db: Session):
        super().__init__()
        self._db = db
        
    def createCompany(self, gln: str, name: str):
        try:
            if len(gln) < 10:
                return {'error':'GLN must be at least 10 characters.','errorValidaror':True}

            if self.company_exist(gln):
                return {'error':'Company alredy registered in RSP.','exist':True}
            
            password = secrets.token_urlsafe(12)
            company = Company(gln=gln, name=name, password=password)
            self._db.add(company)
            self._db.commit()
            self._db.refresh(company)

            return {'success':True, 'company_id': company.id, 'password': company.password}
        except Exception as e:
            self._db.rollback()
            return {'error': str(e)}
    
    def company_exist(self, gln):
        company = self._db.query(Company).filter(Company.gln == gln).first()
        return company is not None

class CompanyMessage(message):
    def __init__(self):
        super().__init__()
