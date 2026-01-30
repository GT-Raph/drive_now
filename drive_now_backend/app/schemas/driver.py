from pydantic import BaseModel, EmailStr

class DriverCreate(BaseModel):
    full_name: str
    email: EmailStr  # 👈 ONLY valid emails allowed
    phone: str
    password: str

class DriverResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str

    class Config:
        from_attributes = True

class DriverDashboard(BaseModel):
    approved: bool
    vehicle_assigned: bool