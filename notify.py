import smtplib, ssl

PORT = 465
USERNAME = "xxx"
PASSWORD = "xxx"

SMTP_ADDRESS = "xxx"

RECIPIENT = "xxx"

def connectToEmailServer():
    """Method to connect to an email server and log in"""
    context = ssl.create_default_context()

    #Connect to the SMTP server
    server = smtplib.SMTP_SSL(SMTP_ADDRESS, PORT, context=context)

    #Log into the server
    server.login(USERNAME, PASSWORD)

    return server

def disconnectEmailServer(server):
    """Method to disconnect from the email server"""
    server.quit()

# Email formal \Subject: {subject} {body}
def sendEmail(server, message):
    """Method to send a email given a server and the message to send"""
    server.sendmail(USERNAME, RECIPIENT, message)

def createEmail(subject, body):
    """Method to create the string format for the email"""
    return "Subject: {}\n\n{}".format(subject, body)