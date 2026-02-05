# DriveNow Backend

This is the FastAPI backend for the DriveNow application.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd drive_now_backend
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   # or manually create .env and copy contents from .env.example
   ```
2. Open `.env` and fill in your credentials:
   - **Database**: Add your PostgreSQL connection string.
   - **Email (Gmail)**:
     - Use your Gmail address.
     - Generate an App Password (NOT your login password).
     - [Guide to get App Password](https://myaccount.google.com/apppasswords)
   - **SMS (Twilio)**:
     - Add your Twilio Account SID and Auth Token.
     - Add your Twilio Phone Number.
     - [Sign up for Twilio Trial](https://www.twilio.com/try-twilio)

### 5. Run the Server

```bash
python -m uvicorn app.main:app --reload
```

## 🔑 OTP Testing (No Setup Required)

Even without configuring Email or SMS, you can test the OTP flow!

- Run the server.
- Request an OTP from the app.
- **Check the Terminal**: The generated OTP code will always be printed in the terminal logs:
  ```
  ✅ [GENERATED OTP] 123456 for user@example.com
  ```
- Use this code to log in.

## 📚 Documentation

- **API Docs**: http://localhost:8000/docs
- **Redoc**: http://localhost:8000/redoc
