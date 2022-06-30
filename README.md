# State Cinema Tickets Notifier (or Notifyer :))
Get email notifications for when new movies at State Cinema have tickets available

## Setup
### notify.py setup
#### Gmail setup
* Create a Google Project in the Google Projects Console
* Enable the Gmail API
* Create the OAuth access token for a Desktop app, and place that into the directory of this program
* Finally follow the steps in Python setup
#### General email setup
* Uncomment the commented code, and comment out the gmail code
* Replace USERNAME and PASSWORD in notify.py with the username and password of the email for notifcations to be sent from
* Find your SMTP address for your email (gmail is smtp.gmail.com) and put that into SMTP_ADDRESS in notify.py
* Finally put the email which you want to send the notifcation to in the RECIPIENT variable


### Python setup
This program only requires Python and Selenium, to install Selenium if Python is a PATH variable open command prompt and type
> pip install selenium

If Python is not a PATH variable, then navigate to where Python is stored and open the Script folder, pip will be in there so open command promt and type
> cd {path to Scripts folder}

> pip install selenium

For Gmail the setup you will also need to install these packages
>   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
