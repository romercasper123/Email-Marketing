import sqlite3
import datetime
import smtplib
from flask import request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def init_db():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            response TEXT,
            timestamp TEXT,
            ip_address TEXT,
            user_agent TEXT
        )
    """)
    con.commit()
    con.close()

def send_consent_email(email):
    # Generate YES and NO URLs
    yes_url = f"http://localhost:5000/consent/yes?email={email}"
    no_url = f"http://localhost:5000/consent/no?email={email}"

    # Load email HTML content and insert links
    with open('templates/consent_email.html', 'r', encoding='utf-8') as file:
        html_content = file.read().replace('{{ yes_url }}', yes_url).replace('{{ no_url }}', no_url)

    # Build email
    message = MIMEMultipart("alternative")
    message["Subject"] = "Do you agree to receive our offers?"
    message["From"] = "tayfabetlog@gmail.com"
    message["To"] = email
    message.attach(MIMEText(html_content, "html"))

    # Send email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("your_email@gmail.com", "password")
            server.sendmail("your_email@gmail.com", email, message.as_string())
    except Exception as e:
        print("Email failed to send:", e)

def log_response(choice):
    email = request.args.get('email')
    ip = request.remote_addr
    agent = request.headers.get('User-Agent')
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    con = sqlite3.connect('database.db')
    cur = con.cursor()

    # ✅ Prevent multiple submissions by email or IP
    cur.execute("SELECT * FROM responses WHERE email = ? OR ip_address = ?", (email, ip))
    existing = cur.fetchone()
    if existing:
        con.close()
        return "⚠️ You have already submitted your response. Thank you!"

    # Log the response
    cur.execute(
        "INSERT INTO responses (email, response, timestamp, ip_address, user_agent) VALUES (?, ?, ?, ?, ?)",
        (email, choice, time, ip, agent)
    )
    con.commit()
    con.close()

    return f"✅ Thank you! Your choice ({choice}) has been recorded."
