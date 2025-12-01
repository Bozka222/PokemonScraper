from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def get_prices(url_dict: dict[str, str]) -> dict[str, str]:
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    prices = {}

    for name, url in url_dict.items():
        print(f"Fetching: {name}")
        try:
            driver.get(url)
            price_element = WebDriverWait(driver, 15).until(
                ec.visibility_of_element_located(
                    (By.XPATH, "//dt[contains(text(), 'From')]/following-sibling::dd[1]")
                )
            )
            price_text = price_element.text.strip()
            prices[name] = price_text
            print(f" → Price: {price_text}")
        except Exception as e:
            print(f"Failed to get price for {name}: {e}")
            prices[name] = None

    driver.quit()
    return prices
