from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from src.config.database import Base

class Registry(Base):
    __tablename__ = "registrymessages"

    id = Column(Integer, primary_key=True, index=True)
    gln = Column(String, index=True)
    gtin = Column(String, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(String, onupdate=func.now())
