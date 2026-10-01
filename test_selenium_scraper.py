import json
from app.scraper.selenium_scraper import scrape_price_selenium

with open("data/products.json", "r") as file:
    products = json.load(file)

iphone = next(product for product in products if product["id"] == 2)

try:
    price = scrape_price_selenium(iphone["url"])
    print("Selenium price:", price)
except Exception as error:
    print("Error:", error)