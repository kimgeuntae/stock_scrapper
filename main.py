# -*- coding: utf-8 -*-

from naver_stocks_list import extract_stock_list_tbody, extract_stock_list_thead, extract_stock_detail_url
from save import save_to_file

MAX_PAGE_NUM = 32
STOCK_LIST_URL = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

stocks_table = []
stocks_table.append(extract_stock_list_thead(f"{STOCK_LIST_URL}{1}"))

for n in range(MAX_PAGE_NUM):
    URL = f"{STOCK_LIST_URL}{n+1}"

    # extract stock list tbody
    for tbody_data in extract_stock_list_tbody(URL):
        stocks_table.append(tbody_data)

save_to_file(stocks_table)