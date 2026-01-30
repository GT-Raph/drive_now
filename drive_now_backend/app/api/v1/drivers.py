from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.driver import Driver
from app.schemas.driver import DriverDashboard

router = APIRouter(prefix="/drivers", tags=["Drivers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/dashboard", response_model=DriverDashboard)
def dashboard(driver_id: int, db: Session = Depends(get_db)):
    driver = db.query(Driver).get(driver_id)
    return DriverDashboard(
        approved=driver.approved_by_admin,
        vehicle_assigned=driver.vehicle_assigned
    )
