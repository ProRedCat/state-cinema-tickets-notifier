import smtplib, ssl

PORT = 465
USERNAME = "xxx"
PASSWORD = "xxx"

SMTP_ADDRESS = "smtp.gmail.com"

RECIPIENT = "xxx"

MESSAGE = """\
Subject: Test Email

This message is sent from Python."""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(SMTP_ADDRESS, PORT, context=context) as server:
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, RECIPIENT, MESSAGE)