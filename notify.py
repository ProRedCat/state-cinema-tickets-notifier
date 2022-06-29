import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

RECIPIENT = "xxx"

CREDENTIALS = 'credentials.json'


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def getService():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Call the Gmail API
    return build('gmail', 'v1', credentials=creds)

def sendEmail(subject, body):
    try:
        # create gmail api client
        service = getService()

        mime_message = MIMEMultipart()
        mime_message["to"] = RECIPIENT
        mime_message["subject"] = subject

        mime_message.attach(MIMEText(body, "plain"))

        raw_string = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()

        service.users().messages().send(userId="me", body={"raw": raw_string}).execute()
    except HttpError as error:
        print(F'An error occurred: {error}')


# import smtplib, ssl

# PORT = 465
# USERNAME = "xxx"
# PASSWORD = "xxx"

# SMTP_ADDRESS = "xxx"

# def connectToEmailServer():
#     """Method to connect to an email server and log in"""
#     context = ssl.create_default_context()

#     #Connect to the SMTP server
#     server = smtplib.SMTP_SSL(SMTP_ADDRESS, PORT, context=context)

#     #Log into the server
#     server.login(USERNAME, PASSWORD)

#     return server

# def disconnectEmailServer(server):
#     """Method to disconnect from the email server"""
#     server.quit()

# # Email formal \Subject: {subject} {body}
# def sendEmail(server, message):
#     """Method to send a email given a server and the message to send"""
#     server.sendmail(USERNAME, RECIPIENT, message)

# def createEmail(subject, body):
#     """Method to create the string format for the email"""
#     return "Subject: {}\n\n{}".format(subject, body)