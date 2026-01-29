from pydantic import BaseModel, EmailStr

class OtpRequest(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    method: str  # email | sms


class OtpVerify(BaseModel):
    otp: str


class CompleteProfile(BaseModel):
    license_number: str
    vehicle_type: str
