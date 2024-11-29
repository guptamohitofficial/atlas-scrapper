from urllib.parse import quote
from app.logger import log
import requests
import json
import os

class Utils:

    def __init__(self, *args, **kwargs):
        self.local_storage_path = kwargs.get("local_storage_path")
        self.products_file_name = "products.json"

    def check_proxied_ip(self, session) -> str:
        try:
            response = session.get(self.get_proxied_url('https://api.ipify.org?format=json'))
            response.raise_for_status()
            ip_info = response.text
            log.debug(ip_info.split('"ip":"')[1].split('"')[0])
            return ip_info.split('"ip":"')[1].split('"')[0]
        except requests.exceptions.RequestException as e:
            log.debug("Failed to check ip error : %s" %str(e))
            return ""

    def get_proxied_url(self, url: str) -> str:
        parsed_url = quote(url, safe='')
        return "https://api.scrapingant.com/v2/general?url=%s&x-api-key=7a5b3b4c1f054ef8b70fd5c2f2c1ae8a" %parsed_url

    def download_image(self, image_url) -> str:
        os.makedirs(self.local_storage_path, exist_ok=True)
        image_name = os.path.basename(image_url)
        save_path = os.path.join(self.local_storage_path, image_name)
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            absolute_path = os.path.abspath(save_path)
            return absolute_path
        except requests.exceptions.RequestException as e:
            log.error("Error downloading image: %s" %str(e))
            return ""

    def add_or_update_product_in_file(self, new_product: dict)->int:
        try:
            with open(self.products_file_name, 'r') as file:
                existing_products = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_products = []
        created_count = 0
        existing_products_dict = {prod['product_title']: prod for prod in existing_products}
        if new_product['title'] in existing_products_dict:
            existing_products_dict[new_product['title']].update(
                product_price=new_product['price'],
                path_to_image=new_product['image_url']
            )
        else:
            created_count += 1
            existing_products_dict[new_product['title']] = {
                "product_title": new_product['title'],
                "product_price": new_product['price'],
                "path_to_image": new_product['image_url'],
            }
        existing_products = list(existing_products_dict.values())
        with open(self.products_file_name, 'w') as file:
            json.dump(existing_products, file, indent=4)
        return created_count
