from fastapi import FastAPI, HTTPException
from app.scraper import Scraper

app = FastAPI()

@app.get("/scrape")
async def scrape_data(token: str = "", limit: int = 5, use_proxy: str = 'false'):
    if token != "atlys-mohit-fixed-token":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized_access - token missing in query param",
        ) 
    base_rul = "https://dentalstall.com/shop"
    scraper = Scraper(limit=limit, base_url=base_rul, use_proxy=(use_proxy == 'true'))
    result = scraper.run()
    return {"message": f"Scraped {result} products."}
