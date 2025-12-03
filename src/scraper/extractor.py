import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


def get_prices(url_dict: dict[str, str]) -> dict[str, str]:
    # options = Options()
    # options.add_argument("--headless=new") # For newer chrome versions
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")  # important for Linux runners
    # options.add_argument("--disable-dev-shm-usage")  # avoid memory issues
    # options.add_argument("--disable-extensions")
    # # options.add_argument('--start-maximized') # Does not work with headless
    # options.add_argument("--window-size=1920,1080")
    # # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument(  # Overrides the headless header to be more real
    #     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    #     "AppleWebKit/537.36 (KHTML, like Gecko) "
    #     "Chrome/120.0.0.0 Safari/537.36"
    # )

    # options.binary_location = "/usr/bin/chromium-browser"  # important for GitHub Actions
    # service = Service('/usr/local/bin/chromedriver')
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = uc.Chrome(options=options)

    prices = {}

    for name, url in url_dict.items():
        print(f"Fetching: {name}")
        try:
            driver.get(url)
            with open("page.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)

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
