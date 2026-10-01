
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlparse


def scrape_price_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)

        domain = urlparse(url).netloc.lower()

        if "amazon." in domain:
            selector = ".a-price-whole"
        elif "flipkart.com" in domain:
            texts = driver.execute_script("""
                    return Array.from(
                        document.querySelectorAll('div')
                    )
                    .map(el => el.textContent.trim())
                    .filter(text => text.startsWith('₹'));
                """)
            price_text = texts[0]
            price_text = price_text.replace("₹", "").replace(",", "").strip()

            return float(price_text)


        else:
            raise ValueError("Website is not supported yet")

        price_element = WebDriverWait(driver, 15).until(
            lambda d: d.find_element(By.CSS_SELECTOR, selector)
        )

        price_text = price_element.get_attribute("textContent")
        price_text = price_text.replace("₹", "").replace(",", "").strip()

        return float(price_text)

    except TimeoutException:
        raise ValueError("Price not found. The website may have changed.")

    finally:
        driver.quit()