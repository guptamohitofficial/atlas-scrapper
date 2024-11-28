import json
import os
import requests
import config as settings
from app.logger import log

OPTS_FILE = "notification/data/whatsapp_opted_in_numbers.json"


class WhatsAppAPIService:

    def __init__(self, base_endpoint, source_phone, app_name, key):
        self.base_endpoint = base_endpoint
        self.source_phone = source_phone
        self.app_name = app_name
        self.key = key

    def load_opted_in_numbers(self) -> set:
        """Load opted-in numbers from a local JSON file."""
        if os.path.exists(OPTS_FILE):
            with open(OPTS_FILE, "r") as file:
                return set(json.load(file))
        return set()

    def save_opted_in_number(self, phone_number: str) -> None:
        """Save an opted-in number to a local JSON file."""
        current_opted_in = self.load_opted_in_numbers()
        current_opted_in.add(phone_number)
        with open(OPTS_FILE, "w") as file:
            json.dump(list(current_opted_in), file)

    def opt_in_and_send_message(self, user_phone: str, template_id: str, template_args: list) -> (bool, str):  # type: ignore
        """Ensure the user is opted in and send a message."""

        if len(user_phone) != 12:
            return False, "Invalid Phone Number"
        is_opted_in = self.check_opt_in_status(user_phone)
        if not is_opted_in:
            if not self.opt_in_user(user_phone):
                return False, "Opt-in Failed"
        data = {
            "channel": "whatsapp",
            "src.name": self.app_name,
            "source": self.source_phone,
            "destination": user_phone,
            "template": json.dumps(
                {
                    "id": template_id,
                    "params": template_args,
                }
            ),
        }
        endpoint = f"{self.base_endpoint}/template/msg"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "apikey": self.key,
        }
        response = requests.post(endpoint, data=data, headers=headers)

        if response.status_code == 200:
            return True, "Success"
        else:
            return False, response.text

    def check_opt_in_status(self, user_phone: str) -> bool:
        """Check if a phone number is already opted in."""
        return user_phone in self.load_opted_in_numbers()

    def opt_in_user(self, user_phone: str) -> bool:
        """Opt a user into WhatsApp notifications."""
        data = {"user": user_phone}
        endpoint = f"{self.base_endpoint}/app/opt/in/{self.app_name}"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "apikey": self.key,
        }
        response = requests.post(endpoint, data=data, headers=headers)
        if response.status_code < 300:
            self.save_opted_in_number(user_phone)
            return True
        return False

    def publish_scrapping_count(self, count: int) -> None:
        log.debug("Sending whatsapp message to users")
        if settings.WHATSAPP_API_KEY:
            for user in settings.NOTIFICATION_USERS:
                if user["is_active"]:
                    print(self.opt_in_and_send_message(
                        f"91{user['whatsapp']}",
                        settings.WHATSAPP_API_TEMPLATE_ID_Atlys_SCRAPPER_NOTIFICATION,
                        [user["name"], count],
                    ))
        else:
            log.error("Whatsapp API key missing")
