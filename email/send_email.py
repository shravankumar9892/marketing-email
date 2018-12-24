import smtplib
import ssl
import getpass                                 
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Details
smtp_server = "smtp.gmail.com"
sender_email = "shravankumarshetty9892@gmail.com"
receiver_email = ["shravankumarshetty9892@gmail.com"]

message = MIMEMultipart("alternative")
message["Subject"] = "BizHub"
message["From"] = sender_email

# If html does not render
text = """\
Hey wassup, it's your boy ET
And welcome to another edition of
Bring it from the bottom Baby,
"THANK GOD it's Monday!"
"""

# Importing the html
with open("index.html") as html:
	html = ' '.join(map(str, list(html)))

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Attaching these to MIMEMultipart
message.attach(part1)
message.attach(part2)

# 465 for SMTP_SSL() and 587 for .starttls()
port = 465 
password = getpass.getpass("Type your password and press enter: \n")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    for receiver in receiver_email:
        message["To"] = receiver	
        server.sendmail(sender_email, receiver, message.as_string())


# NOTE:

#     In case you get an error: smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8 
#     https://support.google.com/mail/?p=BadCredentials y6sm56954094pfd.104 - gsmtp')

#     Go to this link: https://myaccount.google.com/lesssecureapps
#     with your gogole account logged in and click 'enable'
