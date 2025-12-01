import json
from pathlib import Path
from scraper.extractor import get_prices
from scraper.spreadsheet import update_excel

PRODUCTS_PATH = Path("products.json")

# Load products from JSON
with open(PRODUCTS_PATH, "r", encoding="utf-8") as f:
    PRODUCTS = json.load(f)

def main():
    prices = get_prices(url_dict=PRODUCTS)
    update_excel(prices=prices)

if __name__ == "__main__":
    main()
