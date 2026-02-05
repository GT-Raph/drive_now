from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from app.core.config import settings

def send_sms_otp(phone: str, otp: str):
    """
    Send OTP code via SMS using Twilio.
    
    Args:
        phone: Recipient phone number (must include country code, e.g., +233...)
        otp: OTP code to send
    """
    try:
        # Initialize Twilio client
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        # Format the message
        message_body = f"""Your {settings.SMTP_FROM_NAME} verification code is: {otp}

This code will expire in 5 minutes.

Never share this code with anyone!"""
        
        # Send SMS
        message = client.messages.create(
            body=message_body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone
        )
        
        print(f"✅ [SMS OTP] Successfully sent to {phone} -> {otp} (SID: {message.sid})")
        return True
        
    except TwilioRestException as e:
        print(f"❌ [SMS OTP ERROR] Twilio error for {phone}: {e.msg} (Code: {e.code})")
        # Common error codes:
        # 21211 - Invalid phone number
        # 21608 - Phone number is not verified (trial account)
        # 21614 - Invalid phone number format
        return False
        
    except Exception as e:
        print(f"❌ [SMS OTP ERROR] Failed to send to {phone}: {str(e)}")
        return False
