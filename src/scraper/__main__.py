import time
from scraper.extractor import get_prices
from scraper.spreadsheet import update_excel
from pathlib import Path

PRODUCTS = {
    "Groudon HL102": "https://www.cardmarket.com/en/Pokemon/Products/Singles/EX-Hidden-Legends/Groudon-HL102",
    "Groudon ADV-P 026": "https://www.cardmarket.com/en/Pokemon/Products/Singles/ADV-Promos/Groudon-V1",
    "Groudon ADV-P 027": "https://www.cardmarket.com/en/Pokemon/Products/Singles/ADV-Promos/Groudon-V2",
    "Groudon EM 5": "https://www.cardmarket.com/en/Pokemon/Products/Singles/EX-Emerald/Groudon-EM5",
    "Groudon pcgF D007": "https://www.cardmarket.com/en/Pokemon/Products/Singles/Gift-Box-Emerald/Groudon-pcgFD007",
    "Groudon EM 14": "https://www.cardmarket.com/en/Pokemon/Products/Singles/EX-Emerald/Groudon-EM14",
    "Groudon PPB 007": "https://www.cardmarket.com/en/Pokemon/Products/Singles/PokePark-Blue/Groudon",
    "Groudon PCG-P 042": "https://www.cardmarket.com/en/Pokemon/Products/Singles/PCG-Promos/Groudon",
    "Groudon LA 29": "https://www.cardmarket.com/en/Pokemon/Products/Singles/Legends-Awakened/Groudon-Lv45-LA29",
    "Groudon DP5c": "https://www.cardmarket.com/en/Pokemon/Products/Singles/Cry-from-the-Mysterious/Groudon-Lv45-DP5c",
}


def main():
    prices = get_prices(url_dict=PRODUCTS)
    update_excel(prices=prices)

if __name__ == "__main__":
    main()
