from src.services.messageService import messageService, message
from src.services.companyService import CompanyService
from sqlalchemy.orm import Session
from src.models.registry import Registry

class RegistryService(messageService):
    def __init__(self, db: Session):
        super().__init__()
        self._registered = None
        self._db = db

    def registryMessage(self, gln: str, gtin: str, name: str, description: str):

        company_service = CompanyService(self._db)


        if not company_service.company_exist(gln):
            return {'error': 'Company not registered in RSP.'}

        if len(gtin) < 8:
            return {'error': 'GTIN must be at least 8 characters.','errorValidaror':True}

        if self.registry_exists(gtin):
            return {'error': 'GTIN already registered in RSP.'}

        registry = Registry(gtin=gtin, name=name, description=description)
        self._db.add(registry)
        self._db.commit()
        self._db.refresh(registry)
        
        return {'success':True, 'id': registry.id, 'gtin': registry.gtin}        
    
    def registry_exists(self, gtin: str):
        registry = self._db.query(Registry).filter(Registry.gtin == gtin).first()
        return registry is not None
    
class RegistryMessage(message):
    def __init__(self):
        super().__init__()
