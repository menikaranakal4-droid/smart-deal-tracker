import requests
from bs4 import BeautifulSoup


def scrape_price(url):
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=10
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.find("span", class_="price")

    if price_element is None:
        raise ValueError("Price not found on the webpage")

    price_text = price_element.get_text(strip=True)

    price_text = price_text.replace("₹", "").replace(",", "")

    return float(price_text)