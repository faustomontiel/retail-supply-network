from src.services.messageService import messageService, message
from sqlalchemy.orm import Session
from src.models.company import Company
from src.services.hashService import HashService
from src.utils.logs import Logs
import secrets

class CompanyService(messageService):
    def __init__(self, db: Session):
        super().__init__()
        self._db = db
        self._logs = Logs()

    def createCompany(self, gln: str, name: str):
        try:
            self._logs.doLog(f"Start create company")
            
            if len(gln) < 10:
                return {'error':'GLN must be at least 10 characters.','errorValidaror':True}

            if self.company_exist(gln):
                return {'error':'Company alredy registered in RSP.','exist':True}
            
            self._logs.doLog(f"Company validations OK.")

            password = secrets.token_urlsafe(12)
            hashed_password = HashService.hash_password(password)

            company = Company(gln=gln, name=name, password=hashed_password)
            self._db.add(company)
            self._db.commit()
            self._db.refresh(company)

            self._logs.doLog(f"Company added (Commit).")

            return {'success':True, 'company_id': company.id, 'password': password}
        except Exception as e:
            self._db.rollback()
            self._logs.doLog("ERROR createCompany(): " + str(e))
            return {'error': str(e)}
    
    def company_exist(self, gln: str):
        company = self._db.query(Company).filter(Company.gln == gln).first()
        return company is not None
    
    def get_company_password(self, gln: str):
        company = self._db.query(Company).filter(Company.gln == gln).first()
        if company:
            return company.password
        return None

class CompanyMessage(message):
    def __init__(self):
        super().__init__()
