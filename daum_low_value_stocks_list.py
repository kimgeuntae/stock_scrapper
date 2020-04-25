import requests
from bs4 import BeautifulSoup


STOCK_URL = "https://finance.daum.net/domestic/market_cap?market=KOSPI"

result = requests.get(STOCK_URL)

soup = BeautifulSoup(result.text, "html.parser")

all_stock_info = soup.find("div", {"class": "box_type_l"})

