class Cache:
    def __init__(self):
        from collections import defaultdict
        self.price_cache = defaultdict()

    def get_price(self, title: str):
        return self.price_cache.get(title)

    def update_cache(self, product):
        self.price_cache[product.title] = product.price
