from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.db.session import get_db
from app.db.models import Driver, OTP
from app.schemas.auth import OtpRequest, OtpVerify, CompleteProfile
from app.services.otp import generate_otp, get_expiry, OTP_COOLDOWN_SECONDS
from app.services.email import send_email_otp
from app.services.sms import send_sms_otp
from app.core.security import create_access_token

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])


@router.post("/request-otp")
def request_otp(payload: OtpRequest, db: Session = Depends(get_db)):
    existing = db.query(OTP).filter(OTP.email == payload.email).first()

    if existing:
        if datetime.utcnow() - existing.last_sent_at < timedelta(seconds=OTP_COOLDOWN_SECONDS):
            raise HTTPException(status_code=429, detail="Please wait before requesting OTP")
        db.delete(existing)

    otp_code = generate_otp()

    otp = OTP(
        email=payload.email,
        phone=payload.phone,
        code=otp_code,
        expires_at=get_expiry(),
        last_sent_at=datetime.utcnow(),
    )
    db.add(otp)

    driver = db.query(Driver).filter(Driver.email == payload.email).first()
    if not driver:
        driver = Driver(
            full_name=payload.full_name,
            email=payload.email,
            phone=payload.phone,
        )
        db.add(driver)

    db.commit()

    if payload.method == "email":
        send_email_otp(payload.email, otp_code)
    elif payload.method == "sms":
        send_sms_otp(payload.phone, otp_code)
    else:
        raise HTTPException(status_code=400, detail="Invalid OTP method")

    return {"message": "OTP sent"}


@router.post("/verify-otp")
def verify_otp(payload: OtpVerify, db: Session = Depends(get_db)):
    otp = db.query(OTP).filter(OTP.code == payload.otp).first()

    if not otp or otp.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")

    driver = db.query(Driver).filter(Driver.email == otp.email).first()
    driver.is_verified = True

    token = create_access_token({
        "driver_id": driver.id,
        "email": driver.email,
    })

    db.delete(otp)
    db.commit()

    return {
        "access_token": token,
        "profile_completed": driver.profile_completed,
    }


@router.post("/complete-profile")
def complete_profile(
    payload: CompleteProfile,
    driver_id: int = Depends(),  # will be replaced with JWT dependency
    db: Session = Depends(get_db),
):
    driver = db.query(Driver).get(driver_id)
    driver.license_number = payload.license_number
    driver.vehicle_type = payload.vehicle_type
    driver.profile_completed = True
    db.commit()
    return {"message": "Profile completed"}
