
from urllib.parse import urlparse
import re


def validate_product_name(name):
    return isinstance(name, str) and bool(name.strip())


def validate_url(url):
    if not isinstance(url, str):
        return False

    parsed_url = urlparse(url)

    return (
        parsed_url.scheme in ("http", "https")
        and bool(parsed_url.netloc)
        and "." in parsed_url.netloc
    )


def validate_target_price(price):
    try:
        price = float(price)
        return price > 0 and price != float("inf") and price == price
    except (ValueError, TypeError):
        return False


def validate_email(email):
    if not isinstance(email, str):
        return False

    pattern = r"^[\w.+-]+@[\w-]+(?:\.[\w-]+)+$"
    return bool(re.fullmatch(pattern, email))