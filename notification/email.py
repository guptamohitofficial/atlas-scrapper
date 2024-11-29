import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List
from app.logger import log
import config as settings


class EmailClient:
    def __init__(self, smtp_server: str, port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(
        self, subject: str, body: str, to_emails: List[str], from_email: str = None
    ):
        if from_email is None:
            from_email = self.username
        message = MIMEMultipart()
        message["From"] = "Atlys Stuff By Mohit Gupta <%s>" % from_email
        message["To"] = ",".join(to_emails)
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                server.login(self.username, self.password)
                text = message.as_string()
                server.sendmail(from_email, to_emails, text)
                log.debug("Email sent successfully.")
        except Exception as e:
            log.error(f"An error occurred: {e}")

    def publish_scrapping_count(self, count: int, created_scraped: int) -> None:
        log.debug("Sending emails to users")
        for user in settings.NOTIFICATION_USERS:
            if user["is_active"]:
                mail_body = f"""Hi {user['name']},\nMohit's atlys scrapper has scrapped {count} items, created {created_scraped} new products.\nThanks!\nMohit Gupta"""
                self.send_email(
                    "Atlys Scrapper Results", mail_body, [user["email"]], self.username
                )
