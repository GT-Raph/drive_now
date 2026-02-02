from fastapi import FastAPI
from app.api.v1 import drivers, documents
from app.api.v1.routes import router as api_router
from app.admin import approvals
from app.db.session import engine
from app.db.base import Base
from app.models import driver  # 👈 import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DriveNow API",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")
app.include_router(drivers.router)
app.include_router(documents.router)
app.include_router(approvals.router)