import requests
from bs4 import BeautifulSoup


STOCK_URL = "https://finance.naver.com/item/main.nhn?code=005930"

result = requests.get(STOCK_URL)

soup = BeautifulSoup(result.text, "html.parser")

all_stock_info = soup.find("div", {"class": "box_type_l"})

