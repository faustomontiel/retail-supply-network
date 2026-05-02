from src.services.messageService import messageService, message
from src.services.companyService import CompanyService
from sqlalchemy.orm import Session
from src.models.registry import Registry
from src.utils.logs import Logs
import time

class RegistryService(messageService):
    def __init__(self, db: Session):
        super().__init__()
        self._registered = None
        self._db = db
        self._logs = Logs()

    def registryMessage(self, gln: str, gtin: str, name: str, description: str):
        try:
            
            self._logs.doLog("Starting add registry message")
            company_service = CompanyService(self._db)
            
            if not company_service.company_exist(gln):
                return {'error': 'Company not registered in RSP.'}

            self._logs.doLog(f"Company {gln} exist.")

            if len(gtin) < 8:
                return {'error': 'GTIN must be at least 8 characters.','errorValidaror':True}

            if self.registry_exists(gtin):
                return {'error': 'GTIN already registered in RSP.'}

            self._logs.doLog(f"Registry validations OK.")

            registry = Registry(gtin=gtin, name=name, description=description)
            self._db.add(registry)
            self._db.commit()
            self._db.refresh(registry)

            self._logs.doLog(f"Registry added (commit)")

            return {'success':True, 'id': registry.id, 'gtin': registry.gtin}        
        except Exception as e:
            self._db.rollback()
            self._logs.doLog("ERROR registryMessage(): " + str(e))
            return {'error': str(e)} 

    def registry_exists(self, gtin: str):
        registry = self._db.query(Registry).filter(Registry.gtin == gtin).first()
        return registry is not None
    
class RegistryMessage(message):
    def __init__(self):
        super().__init__()
