from notification.email import EmailClient
from notification.whatsapp import WhatsAppAPIService
import config as settings

class Notification:
    def __init__(self, *args, **kwargs) -> None:
        self.email_client = EmailClient(
            settings.SMTP_SERVER,
            settings.SMTP_PORT,
            settings.SMTP_USERNAME,
            settings.SMTP_PASSWORD
        )
        self.whatsapp_client = WhatsAppAPIService(
            settings.WHATSAPP_API_BASE_ENDPOINT,
            settings.WHATSAPP_API_SOURCE_PHONE,
            settings.WHATSAPP_API_APP_NAME,
            settings.WHATSAPP_API_KEY
        )

    def send_notification_everywhere(self, scrapped_products_count: int, created_scraped: int) -> None:
        self.email_client.publish_scrapping_count(scrapped_products_count, created_scraped)
        self.whatsapp_client.publish_scrapping_count(scrapped_products_count, created_scraped)
