from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.driver import Driver
from app.schemas.driver import DriverCreate, DriverResponse
from app.core.security import hash_password
from app.core.security import get_current_driver
from fastapi import UploadFile, File

router = APIRouter()

from app.db.session import get_db

@router.get("/dashboard")
def dashboard(driver=Depends(get_current_driver)):
    return {
        "approved": False, # driver.approved
        "vehicle_assigned": False # driver.vehicle_id is not None
    }

@router.post("/upload-document")
def upload_document(
    type: str,
    file: UploadFile = File(...),
    driver=Depends(get_current_driver)
):
    path = f"uploads/{driver.id}_{type}.jpg"
    with open(path, "wb") as f:
        f.write(file.file.read())
    return {"success": True}

@router.post("/auth/register", response_model=DriverResponse)
def register_driver(
    payload: DriverCreate,
    db: Session = Depends(get_db)
):
    email_exists = db.query(Driver).filter(Driver.email == payload.email).first()
    if email_exists:
        raise HTTPException(status_code=400, detail="Email already registered")

    phone_exists = db.query(Driver).filter(Driver.phone == payload.phone).first()
    if phone_exists:
        raise HTTPException(status_code=400, detail="Phone already registered")

    driver = Driver(
        full_name=payload.full_name,
        email=payload.email,
        phone=payload.phone,
        password_hash=hash_password(payload.password),
    )

    db.add(driver)
    db.commit()
    db.refresh(driver)

    return driver



@router.get("/health")
def health_check():
    return {"status": "ok"}
