import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List
from app.logger import log

class EmailClient:
    def __init__(self, smtp_server: str, port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, subject: str, body: str, to_emails: List[str], from_email: str = None):
        if from_email is None:
            from_email = self.username
        message = MIMEMultipart()
        message['From'] = "Atlas Stuff By Mohit Gupta <%s>" %from_email
        message['To'] = ','.join(to_emails)
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                server.login(self.username, self.password)
                text = message.as_string()
                server.sendmail(from_email, to_emails, text)
                log.debug("Email sent successfully.")
        except Exception as e:
            log.error(f"An error occurred: {e}")


email_client = 

# Details for sending the email
subject = 'Test Email'
body = 'This is a test email sent from Python.'
to_emails = ['recipient1@example.com', 'recipient2@example.com']

# Send the email
email_client.send_email(subject, body, to_emails)