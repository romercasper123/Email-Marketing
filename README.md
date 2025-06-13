
# 📧 Email Consent Manager

A small tool that sends consent request emails and tracks responses.

## ✅ Features
- Sends emails with YES/NO links
- Tracks and stores recipient responses
- SQLite database backend
- Minimal response tracking web endpoint
- Simple protection against multiple submissions (e.g., per IP/email)

## 📂 Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. To Generate a Gmail App Password, Follow These Precise Steps:
📌 Make sure 2-Step Verification is already turned ON, which it seems like you’ve done since you're seeing "Authenticator" and "Google prompt."

🔐 Step-by-Step: Generate Gmail App Password
 Open this link directly:
👉 https://myaccount.google.com/apppasswords

(You may need to log in again.)

 
3.Edit your Gmail credentials in `utils.py`.
Add your Gmail credentials **securely**:
   - Open `utils.py` or wherever your email credentials are used.
   - Replace with your Gmail address and app password (never use your real password):
     ```python
     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
         server.login("your_email@gmail.com", "your_app_password")
         server.sendmail("your_email@gmail.com", email, message.as_string())
     ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Send emails by visiting:
   ```
   http://localhost:5000/send
   ```

## 💾 Stored Format

```json
{
  "email": "john@example.com",
  "response": "YES",
  "timestamp": "2025-06-13 12:45:00",
  "ip_address": "127.0.0.1",
  "user_agent": "Mozilla/5.0..."
}
```

## 📤 Export
Visit `http://localhost:5000/export` to download responses as exel.

