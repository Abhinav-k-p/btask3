# write a python program to send an email with multiple recipients using the smtplib library.

import smtplib
from email.mime.text import MIMEText

email_from = 'akp087@gmail.com'
email_to = ['testing1@gmail.com', 'testing2@gmail.com', 'testing3@gmail.com']
subject = 'This is a testing mail'
body = 'This is an email regarding the testing of sending mail'
message = MIMEText(body)
message['From'] = email_from
message['To'] = ', '.join(email_to) 
message['Subject'] = subject

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = 'e1f25abab1090f'
EMAIL_HOST_PASSWORD = 'e048ee28beb65e'
EMAIL_PORT = '2525'

server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
server.starttls()
server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
server.sendmail(email_from, email_to, message.as_string())
server.quit()
