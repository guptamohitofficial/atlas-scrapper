from notification.email import EmailClient
import config as settings

class Notification:
    def __init__(self, *args, **kwargs):
        self.email_client = EmailClient(settings.SMTP_SERVER, settings.SMTP_PORT, settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
        self.whatsapp_client = None
