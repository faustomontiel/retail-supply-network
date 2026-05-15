from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.config.database import Base

class Publication(Base):
    __tablename__ = "publications"
    id = Column(Integer, primary_key=True, index=True)
    gtin = Column(String, index=True)
    supplier = Column(String, index=True)
    subscriber = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(String, onupdate=func.now())
