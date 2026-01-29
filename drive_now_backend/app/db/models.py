from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.db.base import Base

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)

    is_verified = Column(Boolean, default=False)
    profile_completed = Column(Boolean, default=False)

    license_number = Column(String, nullable=True)
    vehicle_type = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)


class OTP(Base):
    __tablename__ = "otps"

    id = Column(Integer, primary_key=True)
    email = Column(String, index=True)
    phone = Column(String)
    code = Column(String)
    expires_at = Column(DateTime)
    last_sent_at = Column(DateTime, default=datetime.utcnow)
