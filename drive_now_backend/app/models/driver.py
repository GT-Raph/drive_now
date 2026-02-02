from app.db.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=True)
    # is_verified = Column(Boolean, default=False)

    # profile completion
    # license_number = Column(String, nullable=True)
    # vehicle_type = Column(String, nullable=True)
    # profile_completed = Column(Boolean, default=False)
    # vehicle_assigned = Column(Boolean, default=False)
    # created_at = Column(DateTime, default=datetime.utcnow)


class OTP(Base):
    __tablename__ = "otps"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    code = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    last_sent_at = Column(DateTime, default=datetime.utcnow)
