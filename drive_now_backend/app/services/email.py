import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import settings

def send_email_otp(email: str, otp: str):
    """
    Send OTP code via email using SMTP.
    
    Args:
        email: Recipient email address
        otp: OTP code to send
    """
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f'Your {settings.SMTP_FROM_NAME} Verification Code'
        msg['From'] = f'{settings.SMTP_FROM_NAME} <{settings.SMTP_USER}>'
        msg['To'] = email
        
        # Create HTML email template
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    max-width: 600px;
                    margin: 40px auto;
                    background-color: #ffffff;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                    overflow: hidden;
                }}
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    text-align: center;
                }}
                .content {{
                    padding: 40px 30px;
                    text-align: center;
                }}
                .otp-code {{
                    font-size: 36px;
                    font-weight: bold;
                    color: #667eea;
                    letter-spacing: 8px;
                    padding: 20px;
                    background-color: #f8f9fa;
                    border-radius: 8px;
                    margin: 20px 0;
                    display: inline-block;
                }}
                .footer {{
                    background-color: #f8f9fa;
                    padding: 20px;
                    text-align: center;
                    color: #666;
                    font-size: 12px;
                }}
                .warning {{
                    color: #e74c3c;
                    font-size: 14px;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>{settings.SMTP_FROM_NAME}</h1>
                    <p>Verification Code</p>
                </div>
                <div class="content">
                    <h2>Your OTP Code</h2>
                    <p>Use the following code to complete your verification:</p>
                    <div class="otp-code">{otp}</div>
                    <p>This code will expire in <strong>5 minutes</strong>.</p>
                    <p class="warning">⚠️ Never share this code with anyone!</p>
                </div>
                <div class="footer">
                    <p>If you didn't request this code, please ignore this email.</p>
                    <p>&copy; 2026 {settings.SMTP_FROM_NAME}. All rights reserved.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Plain text version for email clients that don't support HTML
        text = f"""
        {settings.SMTP_FROM_NAME} - Verification Code
        
        Your OTP Code: {otp}
        
        This code will expire in 5 minutes.
        Never share this code with anyone!
        
        If you didn't request this code, please ignore this email.
        """
        
        # Attach both versions
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        
        # Send email
        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.send_message(msg)
        
        print(f"✅ [EMAIL OTP] Successfully sent to {email} -> {otp}")
        return True
        
    except Exception as e:
        print(f"❌ [EMAIL OTP ERROR] Failed to send to {email}: {str(e)}")
        # In production, you might want to log this to a file or monitoring service
        # For now, we'll just print and continue (OTP is still in database)
        return False
