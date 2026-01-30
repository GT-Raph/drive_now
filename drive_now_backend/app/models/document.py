from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base
from pydantic import BaseModel

class DriverDocument(Base):
    __tablename__ = "driver_documents"

    id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey("drivers.id"))
    doc_type = Column(String)  # license, ghana_card, selfie, utility
    file_url = Column(String)

class DocumentUpload(BaseModel):
    doc_type: str
    file_url: str