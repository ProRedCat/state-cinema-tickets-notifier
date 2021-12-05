# State Cinema Tickets Notifyer
Get email notifications for when new movies at State Cinema have tickets available

## Setup
### notify.py setup
* Replace USERNAME and PASSWORD in notify.py with the username and password of the email for notifcations to be sent from. This program does not use OAuth so if using a gmail account you must allow less secure apps on that account
* Find your SMTP address for your email (gmail is smtp.gmail.com) and put that into SMTP_ADDRESS in notify.py
* Finally put the email which you want to send the notifcation to in the RECIPIENT variable
### Python setup
This program only requires Python and Selenium, to install Selenium if Python is a PATH variable open command prompt and type
> pip install selenium

If Python is not a PATH variable, then navigate to where Python is stored and open the Script folder, pip will be in there so open command promt and dtype
> cd {path to Scripts folder}

> pip install selenium
