from src.services.messageService import messageService, message
from sqlalchemy.orm import Session
from src.models.registry import Registry

class RegistryService(messageService):
    def __init__(self, db: Session):
        super().__init__()
        self._registered = None
        self._db = db

    def registryMessage(self, gtin: str, name: str, description: str):
        registry = Registry(gtin=gtin, name=name, description=description)
        self._db.add(registry)
        self._db.commit()
        self._db.refresh(registry)
        return registry        

class RegistryMessage(message):
    def __init__(self):
        super().__init__()
