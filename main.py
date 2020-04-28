# -*- coding: utf-8 -*-

from datetime import datetime
from naver_stocks_list import extract_stock_list_tbody, extract_stock_list_thead, extract_stock_detail_url
from save import save_list_to_file
from stock_evaluation import is_over, is_under, check_low_stock
from daum_stock_detail import extract_stock_detail_dict
PRICE_STANDARD = 100000   # 현재가
DIFF_STANDARD = []    # 전일비
FLUC_STANDARD = []    # 등락률
PAR_STANDARD = []  # 액면가
CAPITALIZATION_STANDARD = 1000  # 시가총액
TOTAL_STOCKS_STANDARD = []   # 상장 주식수
FOREIGN_STANDARD = [] # 외국인 비율
VOLUME_STANDARD = []  # 거래량
PER_STANDARD = 10     # PER
ROE_STANDARD = 5  # ROE

MAX_PAGE_NUM = 32
STOCK_LIST_URL = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=" # stock number

STOCK_FUNDAMENTAL_URL = "https://finance.naver.com/item/coinfo.nhn?code="   # stock number

TODAY = datetime.today().strftime("%Y%m%d")
CSV_FORDER = "rank_csv"
FILE_FORMAT = "csv"
FNAME_CAPITALIZATION_RANK = f"{TODAY}_capitalization_rank"
FNAME_LOW_VALUATION_LIST = f"{TODAY}_low_valuation_list"
FNAME_ACCEPTED_PER_ROE_LIST = f"{TODAY}_accepted_PER_ROE_list"
FNAME_CAPI_OVER_STANDARD_STOCKS = f"{TODAY}_capi_over_{CAPITALIZATION_STANDARD}_stocks"

capi_rank_stocks_table = []
low_value_list = []

capi_rank_thead = extract_stock_list_thead(f"{STOCK_LIST_URL}{1}")
capi_rank_tbody = []

capi_rank_stocks_table.append(capi_rank_thead)
low_value_list.append(capi_rank_thead)

low_stocks_list = []
temp_stocks_list = []

temp_list = []

# build capi_rank_stocks_table
for n in range(MAX_PAGE_NUM):
    URL = f"{STOCK_LIST_URL}{n+1}"

    # extract stock list tbody
    for tbody_data in extract_stock_list_tbody(URL):
        capi_rank_tbody.append(tbody_data)
        capi_rank_stocks_table.append(tbody_data)

########### SAVE CAPITALIZATION_RANK ###########
save_list_to_file(f"{CSV_FORDER}/{FNAME_CAPITALIZATION_RANK}.{FILE_FORMAT}", capi_rank_stocks_table)


# build capi_over_standard_stocks
temp_stocks_list.append(capi_rank_thead)

for stock in capi_rank_tbody:
    temp_capi = stock[6].replace(",","")
    if is_over(temp_capi, CAPITALIZATION_STANDARD):
        temp_list.append(stock)
        temp_stocks_list.append(stock)

########### SAVE CAPI_OVER_STANDARD_STOCKS ###########
save_list_to_file(f"{CSV_FORDER}/{FNAME_CAPI_OVER_STANDARD_STOCKS}.{FILE_FORMAT}", temp_stocks_list)


# build accept_PER_ROE_LIST
temp_stocks_list.clear()
temp_stocks_list.append(capi_rank_thead)

for stock in temp_list:
    temp_PER = stock[10].replace(",", "")
    temp_ROE = stock[11].replace(",", "")
    
    if is_under(temp_PER, PER_STANDARD):
        if is_over(temp_ROE, ROE_STANDARD):
            temp_stocks_list.append(stock)

temp_list = temp_stocks_list[1:-1]

print(f"{FNAME_ACCEPTED_PER_ROE_LIST} : {len(temp_list)}")
########### SAVE accepted PER, ROE ###########
save_list_to_file(f"{CSV_FORDER}/{FNAME_ACCEPTED_PER_ROE_LIST}.{FILE_FORMAT}", temp_stocks_list)


# build low_stock_list
low_stocks_list.append(capi_rank_thead)

for idx, stock in enumerate(temp_list):
    # get index, value from enumerate
    print(idx+1, stock[1])
    temp_stock_dict = extract_stock_detail_dict(stock[-1])
    
    if check_low_stock(stock, temp_stock_dict["year_financial"]):
        if check_low_stock(stock, temp_stock_dict["quarter_financial"]):
            low_stocks_list.append(stock)

########### SAVE checked low stock list ###########
save_list_to_file(f"{CSV_FORDER}/{FNAME_LOW_VALUATION_LIST}.{FILE_FORMAT}", low_stocks_list)



