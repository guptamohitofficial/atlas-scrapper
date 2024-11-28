from fastapi import FastAPI
from app.scraper import Scraper

app = FastAPI()

@app.get("/scrape")
async def scrape_data(limit: int = 5):
    base_rul = "https://dentalstall.com/shop"
    scraper = Scraper(limit=limit, base_url=base_rul)
    result = scraper.run()
    return {"message": f"Scraped {result} products."}
