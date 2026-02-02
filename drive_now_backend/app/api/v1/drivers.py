from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.driver import Driver
from app.schemas.driver import DriverDashboard

from app.schemas.auth import CompleteProfile
from app.core.security import get_current_driver

router = APIRouter(prefix="/api/v1/drivers", tags=["Drivers"])

from app.db.session import get_db

@router.get("/dashboard", response_model=DriverDashboard)
def dashboard(driver_id: int, db: Session = Depends(get_db)):
    driver = db.query(Driver).get(driver_id)
    return DriverDashboard(
        approved=False, # driver.approved_by_admin,
        vehicle_assigned=False # driver.vehicle_assigned
    )

@router.post("/complete-profile")
def complete_profile(
    payload: CompleteProfile,
    driver: Driver = Depends(get_current_driver),
    db: Session = Depends(get_db),
):
    driver.license_number = payload.license_number
    driver.vehicle_type = payload.vehicle_type
    driver.profile_completed = True
    db.commit()
    return {"message": "Profile completed"}
