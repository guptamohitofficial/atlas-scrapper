import json
from app.models import Product

class Database:
    def __init__(self):
        self.filepath = 'products.json'
        self.load()

    def load(self):
        try:
            with open(self.filepath, 'r') as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []

    def save_product(self, product: Product):
        for prod in self.data:
            if prod['title'] == product.title:
                prod.update(product.dict())
                break
        else:
            self.data.append(product.dict())
        self.save()

    def save(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.data, file, indent=4)