
from bs4 import BeautifulSoup
from typing import List
from app.models import Product
from app.database import Database
from app.cache import Cache
from app.utils import Utils
from app.logger import log
from notification import Notification
import config as settings
import requests
import time 

class Scraper:
    def __init__(self, limit: int, base_url: str, use_proxy: bool = False):
        self.limit = limit
        self.db = Database()
        self.cache = Cache()
        self.use_proxy = use_proxy
        self.utils = Utils(local_storage_path='saved_media')
        self.base_url = base_url
        self.notification = Notification()

    def run(self) -> int:
        total_scraped = 0
        created_scraped = 0
        for page in range(1, self.limit + 1):
            log.debug("Scrapping page number %d" %page)
            if page == 1:
                url = f"{self.base_url}"
            else:
                url = f"{self.base_url}/page/{page}"
            products = self.scrape_page(url)
            if products:
                total_scraped += len(products)
                created_scraped += self.process_products(products)
        if settings.DEBUG:
            log.info(f"Scrapping completed, {total_scraped} products scrapped, {created_scraped} were newly created")
        else:
            self.notification.send_notification_everywhere(total_scraped, created_scraped)
        return total_scraped
    
    def scrape_page(self, url: str) -> List[Product]:
        """Scrape a single page and return a list of Product objects."""
        session = requests.Session()
        retries = 3
        while retries:
            try:
                if self.use_proxy: # free proxy server is being used, its a little slow
                    log.debug("Fetching page with proxy")
                    response = session.get(self.utils.get_proxied_url(url))
                else:
                    log.debug("Fetching page without proxy")
                    response = session.get(url)
                log.debug("Page fetched")
                response.raise_for_status()
                return self.parse_products(response.text)
            except requests.exceptions.RequestException as e:
                log.error("Request failed: %s, retrying in a few seconds..." %str(e))
                retries -= 1
                time.sleep(5)

        return []

    def parse_products(self, html: str) -> List[Product]:
        """Parse HTML content to extract product information."""
        soup = BeautifulSoup(html, "html.parser")
        products = []
        for item in soup.select("li.product"):
            title_elem = item.select_one(".woo-loop-product__title a")
            title = title_elem.get_text(strip=True) if title_elem else "N/A"

            price = 0
            price_elem = item.select_one(".price .woocommerce-Price-amount")
            if price_elem:
                price_text = price_elem.get_text(strip=True).replace("₹", "").replace(",", "")
                try:
                    price = float(price_text)
                except ValueError as error:
                    log.error("Failed parsing price for %s, error: %s" %(title, str(error)))

            image_elem = item.select_one(".mf-product-thumbnail img")
            image_url = image_elem["data-lazy-src"] if image_elem else ""
            if image_url:
                image_path = self.utils.download_image(image_url)
            product = {"title":title, "price":price, "image_url":image_path}
            products.append(product)
        return products

    def process_products(self, products: List[Product]) -> int:
        """Process the list of products for updates and caching."""
        updated_count = 0
        for product in products:
            count_to_update = 0
            cached_price = self.cache.get_price(product['title'])
            if cached_price is None or cached_price != product['title']:
                if settings.DEBUG:
                    count_to_update = self.utils.add_or_update_product_in_file(product)
                else:
                    count_to_update = self.db.add_or_update_product(product)
                self.cache.update_cache(product)
                updated_count += count_to_update
        return updated_count
