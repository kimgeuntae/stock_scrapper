# -*- coding: utf-8 -*-

from naver_stocks_list import extract_stock_list_tbody, extract_stock_list_thead, extract_stock_detail_url
from save import save_list_to_file
from stock_evaluation import is_over

MAX_PAGE_NUM = 32
STOCK_LIST_URL = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

CSV_FORDER = "rank_csv"
FILE_FORMAT = "csv"
FNAME_CAPITALIZATION_RANK = "capitalization_rank"
FNAME_LOW_VALUATION_LIST = "low_valuation _list"
FNAME_CAPI_OVER_3000_STOCKS = "capi_over_3000_stocks"

PRICE_STANDARD = 100000   # 현재가
DIFF_STANDARD = []    # 전일비
FLUC_STANDARD = []    # 등락률
PAR_STANDARD = []  # 액면가
CAPI_STANDARD = 3000  # 시가총액
TOTAL_STANDARD = []   # 상장 주식수
FOREIGN_STANDARD = [] # 외국인 비율
VOLUME_STANDARD = []  # 거래량
PER_STANDARD = []     # PER
ROE_STANDARD = []  # ROE

capi_rank_stocks_table = []
low_value_list = []

capi_rank_thead = extract_stock_list_thead(f"{STOCK_LIST_URL}{1}")
capi_rank_tbody = []

capi_rank_stocks_table.append(capi_rank_thead)
low_value_list.append(capi_rank_thead)

temp_check_low_stocks_list = []

for n in range(MAX_PAGE_NUM):
    URL = f"{STOCK_LIST_URL}{n+1}"

    # extract stock list tbody
    for tbody_data in extract_stock_list_tbody(URL):
        capi_rank_tbody.append(tbody_data)
        capi_rank_stocks_table.append(tbody_data)

########### SAVE CAPITALIZATION_RANK ###########
save_list_to_file(f"{CSV_FORDER}/{FNAME_CAPITALIZATION_RANK}.{FILE_FORMAT}", capi_rank_stocks_table)


for stock_list in capi_rank_tbody:
    temp_capi = stock_list[6].replace(",","")
    if is_over(temp_capi, CAPI_STANDARD):
        temp_check_low_stocks_list.append(stock_list)

########### SAVE CAPI_OVER_3000_STOCKS ###########
save_list_to_file(f"{CSV_FORDER}/{FNAME_CAPI_OVER_3000_STOCKS}.{FILE_FORMAT}", temp_check_low_stocks_list)

