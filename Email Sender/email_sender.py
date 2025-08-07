import smtplib
from email.mime.text import MIMEText
current_email = MIMEText('This is a test email sent from Python!')
current_email['Subject'] = 'Test Email'
current_email['From'] = 'Your gmail'
current_email['To'] = 'who you want to send'

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login('Your gmail','key pass on your gmail')
    server.send_message(current_email)
    print("Email sent successfully!")
