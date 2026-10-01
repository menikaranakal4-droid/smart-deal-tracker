from app.scraper.beautifulsoup_scraper import scrape_price

url = "http://127.0.0.1:5000/test-price"

try:
    price = scrape_price(url)
    print("Scraped Price:", price)
except Exception as error:
    print("Error:", error)




