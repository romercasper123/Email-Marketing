
from flask import Flask, request, render_template
import sqlite3
import datetime
import os
from utils import send_consent_email, log_response

app = Flask(__name__)

@app.route('/')
def home():
    return 'Email Consent Manager Running!'

@app.route('/send')
def send():
    import csv
    with open('emails.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            send_consent_email(row['email'])
    return 'Emails sent!'

@app.route('/consent/yes')
def consent_yes():
    return log_response("YES")

@app.route('/consent/no')
def consent_no():
    return log_response("NO")

@app.route('/export')
def export_csv():
    import csv
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT email, response, timestamp, ip_address, user_agent FROM responses")
    rows = cur.fetchall()
    con.close()

    from flask import Response
    def generate():
        yield 'email,response,timestamp,ip_address,user_agent\n'
        for row in rows:
            yield ','.join(row) + '\n'
    return Response(generate(), mimetype='text/csv', headers={"Content-Disposition": "attachment;filename=responses.csv"})

if __name__ == '__main__':
    from utils import init_db
    init_db()
    app.run(debug=True)
