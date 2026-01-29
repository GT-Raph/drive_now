import random
from datetime import datetime, timedelta

OTP_EXPIRY_MINUTES = 5
OTP_COOLDOWN_SECONDS = 60

def generate_otp() -> str:
    return str(random.randint(100000, 999999))

def get_expiry():
    return datetime.utcnow() + timedelta(minutes=OTP_EXPIRY_MINUTES)
