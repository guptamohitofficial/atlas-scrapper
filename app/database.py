from peewee import IntegrityError
from app.models import Product
from app.logger import log

class Database:

    def add_or_update_product(self, product_data) -> int:
        """Add a new product or update an existing product by title."""
        try:
            created_count = 0
            product, created = Product.get_or_create(
                title=product_data['title'],
                defaults=product_data
            )
            if not created:
                query = Product.update(
                    price=product_data['price'],
                    image_url=product_data['image_url']
                ).where(Product.title == product_data['title'])
                query.execute()
            else:
                created_count = 1
            return created_count
        except IntegrityError as e:
            log.error("Error with database operation: %s" %str(e))
            return 0 
