import smtplib, ssl

PORT = 465
USERNAME = "xxx"
PASSWORD = "xxx"

SMTP_ADDRESS = "xxx"

RECIPIENT = "xxx"

def connectToEmailServer():
    context = ssl.create_default_context()

    server = smtplib.SMTP_SSL(SMTP_ADDRESS, PORT, context=context)
    server.login(USERNAME, PASSWORD)

    return server

def disconnectEmailServer(server):
    server.quit()

# Email formal \Subject: {subject} {body}
def sendEmail(server, message):
    server.sendmail(USERNAME, RECIPIENT, message)

def createEmail(subject, body):
    return "Subject: {}\n\n{}".format(subject, body)