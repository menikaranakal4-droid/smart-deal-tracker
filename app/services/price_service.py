from app.scraper.beautifulsoup_scraper import scrape_price
from app.scraper.selenium_scraper import scrape_price_selenium
from datetime import datetime
from app.services.email_service import send_price_alert
import requests

def check_price(product):
    try:
        if product.get("scraper") == "selenium":
            current_price = scrape_price_selenium(product["url"])
        else:
            current_price = scrape_price(product["url"])
    except (ValueError, requests.RequestException) as error:
        raise ValueError(f"Price check failed: {error}") from error

    target_price = product["target_price"]
    product["current_price"] = current_price

    if current_price <= target_price:
        status = "Target price reached"
        product["current_price"] = current_price
        if not product.get("alert_sent", False):
            send_price_alert(product)
            product["alert_sent"] = True
    else:
        status = "Target price not reached"

    if "price_history" not in product:
        product["price_history"] = []

    product["price_history"].append({
        "price": current_price,
        "timestamp": datetime.now().isoformat()
    })

    return current_price, status

