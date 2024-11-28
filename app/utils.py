from urllib.parse import quote
import requests
import os

class Utils:
    def __init__(self, *args, **kwargs):
        local_storage_path = kwargs.get("local_storage_path")
    
    def check_proxied_ip(self, session) -> str:
        try:
            response = session.get(self.get_proxied_url('https://api.ipify.org?format=json'))
            response.raise_for_status()
            ip_info = response.text
            print(ip_info.split('"ip":"')[1].split('"')[0])
            return ip_info.split('"ip":"')[1].split('"')[0]
        except requests.exceptions.RequestException as e:
            print(e)
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
            print(f"Error downloading image: {e}")
            return ""

    
