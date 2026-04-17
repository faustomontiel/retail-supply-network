from services.messageService import messageService, message
from sqlalchemy.orm import Session
from models.registry import Registry

class registryService(messageService):
    def __init__(self, db: Session):
        self._registered = None
        self._db = db
        super().__init__()

    def registryMessage(self, gtin: str, name: str, description: str):
        registry = Registry(gtin=gtin, name=name, description=description)
        self._db.add(registry)
        self._db.commit()
        self._db.refresh(registry)
        return registry        

class registryMessage(message):
    def __init__(self):
        super().__init__()
