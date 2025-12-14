import smtplib
from email.message import EmailMessage
import os

def send_email(subject, body, is_html=False):
    msg = EmailMessage()
    msg["From"] = os.getenv("EMAIL")
    msg["To"] = os.getenv("EMAIL")
    msg["Subject"] = subject

    if is_html:
        msg.add_alternative(body, subtype='html')
    else:
        msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
        server.send_message(msg)
