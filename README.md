# Pokemon Card Price Scraper

This Python project scrapes Pokémon card prices from [Cardmarket](https://www.cardmarket.com) and updates an Excel spreadsheet with the latest values. 

---

## Features

- Scrapes prices for multiple Pokémon cards.
- Uses Selenium to fetch dynamic content from the website.
- Updates an Excel file (`my_prices.xlsx`) with:
  - Product names (column A)
  - Current price (column B)
  - Timestamp of the last update (column C)

---

## Requirements

- Python 3.10+
- `selenium`
- `openpyxl`
- Chrome browser installed
- ChromeDriver matching your Chrome version

Install Python dependencies with:

```bash
pip install -r requirements.txt
