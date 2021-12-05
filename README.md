# State Cinema Tickets Notifyer
Get email notifications for when new movies at State Cinema have tickets available

## Setup
### All the setup required is in notify.py
* Replace USERNAME and PASSWORD in notify.py with the username and password of the email for notifcations to be sent from. This program does not use OAuth so if using a gmail account you must allow less secure apps on that account
* Find your SMTP address for your email (gmail is smtp.gmail.com) and put that into SMTP_ADDRESS in notify.py
* Finally put the email which you want to send the notifcation to in the RECIPIENT variable

