from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.document import DriverDocument

router = APIRouter(prefix="/documents", tags=["Documents"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload/{driver_id}")
async def upload_document(
    driver_id: int,
    doc_type: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    path = f"uploads/{driver_id}_{doc_type}.jpg"
    with open(path, "wb") as f:
        f.write(await file.read())

    doc = DriverDocument(driver_id=driver_id, doc_type=doc_type, file_url=path)
    db.add(doc)
    db.commit()
    return {"success": True, "file_url": path}
