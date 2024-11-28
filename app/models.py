from pydantic import BaseModel, validator

class Product(BaseModel):
    title: str
    price: float
    image_url: str

    @validator('price')
    def price_must_be_positive(cls, price):
        if price < 0:
            raise ValueError('Price must be positive')
        return price
