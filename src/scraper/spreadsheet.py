import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

def update_excel(prices: dict[str, str]) -> None:
    # Authenticate
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets", # Editing
        "https://www.googleapis.com/auth/drive" # List/Open by name
    ]
    CREDS = Credentials.from_service_account_file("service_account.json", scopes=SCOPES)
    gc = gspread.authorize(CREDS)

    sh = gc.open("PokemonScraper")
    ws = sh.worksheet("List 1")


    # Loop over rows and update column B and C
    records = ws.get_all_records()
    for i, row in enumerate(records, start=2):  # start=2 because row 1 is header
        product_name = row['Product Name']  # assuming column A header is "Product Name"
        if product_name in prices:
            ws.update(values=[[prices[product_name]]], range_name=f"B{i}")
            ws.update(values=[[datetime.now().strftime("%Y-%m-%d")]], range_name=f"C{i}")

    print("Excel updated ✔")
