# 📧 Email Consent Manager

A lightweight tool to manage email consent by sending request emails and tracking user responses.

## ✅ Features
- 📩 Sends consent request emails with **YES/NO** links  
- 🗂️ Tracks and stores recipient responses  
- 💾 Uses SQLite as the backend database  
- 🌐 Minimal web endpoint for response tracking  
- 🔐 Prevents multiple submissions by IP or email

## ⚙️ Setup Instructions

### 1. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Gmail for Sending Emails

To send emails securely using your Gmail account:

#### 📌 Requirements:
- Make sure **2-Step Verification** is enabled on your Gmail account.

#### 🔐 Generate a Gmail App Password:
1. Visit: 👉 https://myaccount.google.com/apppasswords
2. Sign in if prompted.
3. Select “Mail” as the app and “Other” (custom name) as the device (e.g., `EmailConsentApp`).
4. Click **Generate** and copy the 16-character app password.

### 3. Add Your Gmail Credentials

Open the file `utils.py` (or wherever your email credentials are stored), and replace the login credentials:
```python
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login("your_email@gmail.com", "your_app_password")
    server.sendmail("your_email@gmail.com", email, message.as_string())
```

### 4. Add Recipient Emails

Create or edit `emails.csv` with the following format:

**emails.csv**
```
email
tayfasaltik@gmail.com
redforwhite@gmail.com
```

### 5. Run the Application
```bash
python app.py
```

### 6. Trigger Email Sending
Visit the following URL in your browser to send consent emails:
```
http://localhost:5000/send
```

## 💾 Response Storage Format

Responses are saved in the SQLite database with the following structure:
```json
{
  "email": "john@example.com",
  "response": "YES",
  "timestamp": "2025-06-13 12:45:00",
  "ip_address": "127.0.0.1",
  "user_agent": "Mozilla/5.0..."
}
```

## 📤 Exporting Responses

To download all recorded responses in Excel format, visit:
```
http://localhost:5000/export
```

---

## 🧱 SQLite Setup

This project uses SQLite for storing email responses. SQLite is lightweight and requires no server installation.

### 🔽 Download SQLite:

- **Windows**:  
  👉 https://www.sqlite.org/download.html  
  Download the **Precompiled Binaries for Windows**, extract it, and place `sqlite3.exe` in your project folder or somewhere in your system PATH.

- **macOS** (usually pre-installed):  
  To verify, run in Terminal:  
  ```bash
  sqlite3 --version
  ```

- **Linux**:  
  Install using package manager:  
  ```bash
  sudo apt install sqlite3
  ```

### 📦 Usage
You don’t need to manually create the database — it will be automatically created when you run `app.py`.

To inspect the database manually:
```bash
sqlite3 database.db
.tables
SELECT * FROM responses;
```
