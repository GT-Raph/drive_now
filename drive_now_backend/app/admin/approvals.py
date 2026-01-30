from fastapi import APIRouter
from app.core.database import SessionLocal
from app.models.driver import Driver

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/approve-driver/{driver_id}")
def approve_driver(driver_id: int):
    db = SessionLocal()
    driver = db.query(Driver).get(driver_id)
    driver.approved_by_admin = True
    db.commit()
    return {"message": "Driver approved"}
