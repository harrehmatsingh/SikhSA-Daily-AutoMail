import hukum
import os
from dotenv import load_dotenv
# Send the mail
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime

load_dotenv()

now = datetime.datetime.now()

# Load environment variables from .env if present
load_dotenv()

# email content placeholder
content = '<b>Golden Temple Hukumnama:</b>\n'+'<br>'+'-'*50+'<br>'

cnt = hukum.getHukum()
content += cnt
content += ('<br>------<br>')
content +=('<br><br>End of Message')


#lets send the email
print('Composing Email...')

SERVER = 'smtp.gmail.com' # the smtp server
PORT = 587 # smtp port number for gmail
TO =  os.getenv("TO_EMAIL_ADDRESS") # "from email id"
FROM = os.getenv("FROM_EMAIL_ADDRESS") # "to email ids"  # can be a list
PASS = os.getenv("PASS") # google account's app password

msg = MIMEMultipart()

msg['Subject'] = 'UMSIKHSA' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(
    now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.ehlo()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()
