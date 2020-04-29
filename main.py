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
KOSPI_CAPITALIZATION_STANDARD = 1500	  # KOSPI 시가총액
KOSDAQ_CAPITALIZATION_STANDARD = 350  # KOSDAQ 시가총액
TOTAL_STOCKS_STANDARD = []   # 상장 주식수
FOREIGN_STANDARD = [] # 외국인 비율
VOLUME_STANDARD = []  # 거래량
PER_STANDARD = 10     # PER
ROE_STANDARD = 5  # ROE

KOSPI = 0
KOSDAQ = 1

KOSPI_MAX_PAGE_NUM = 32
KOSDAQ_MAX_PAGE_NUM = 29

KOSPI_STOCK_LIST_URL = f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok={KOSPI}&page="
KOSDAQ_STOCK_LIST_URL = f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok={KOSDAQ}&page="

TODAY = datetime.today().strftime("%Y%m%d")
CSV_FORDER = "rank_csv"
FILE_FORMAT = "csv"

FNAME_CAPITALIZATION_RANK = f"capitalization_rank"
FNAME_LOW_VALUATION_LIST = f"low_valuation_list"
FNAME_ACCEPTED_PER_ROE_LIST = f"accepted_PER_ROE_list"


def extract_stock_thead(URL):
    stock_thead = extract_stock_list_thead(f"{URL}{1}")
    return stock_thead


def extract_stock_capitalization_rank(URL, max_page_num):
    capi_rank_stocks = []
    capi_rank_stocks.append(extract_stock_thead(URL))

    # build capi_rank_stocks_table
    for n in range(max_page_num):
        tenmp_URL = f"{URL}{n+1}"
        # extract stock list tbody
        for tbody_data in extract_stock_list_tbody(tenmp_URL):
            capi_rank_stocks.append(tbody_data)

    return capi_rank_stocks


def extract_over_capi_standard_stocks(temp_stocks_list, capi_standard):
    over_capi_standard_stocks = []
    over_capi_standard_stocks.append(temp_stocks_list[0])

    tbody = temp_stocks_list[1:-1]

    # build over_capi_standard_stocks
    for stock in tbody:
        temp_capi = stock[6].replace(",","")
        if is_over(temp_capi, capi_standard):
            over_capi_standard_stocks.append(stock)
    
    return over_capi_standard_stocks


def extract_accept_PER_ROE_list(temp_stocks_list):
    accept_PER_ROE_stocks = []
    accept_PER_ROE_stocks.append(temp_stocks_list[0])

    tbody = temp_stocks_list[1:-1]

    # build accept_PER_ROE_LIST
    for stock in tbody:
        temp_PER = stock[10].replace(",", "")
        temp_ROE = stock[11].replace(",", "")
        
        if is_under(temp_PER, PER_STANDARD):
            if is_over(temp_ROE, ROE_STANDARD):
                accept_PER_ROE_stocks.append(stock)

    print(f"{FNAME_ACCEPTED_PER_ROE_LIST} : {len(accept_PER_ROE_stocks)-1}")
    return accept_PER_ROE_stocks
    

def extract_accepted_low_value_stocks(temp_stocks_list):
    low_stocks_list = []
    low_stocks_list.append(temp_stocks_list[0])
    
    tbody = temp_stocks_list[1:-1]

    # build low_stock_list
    for idx, stock in enumerate(tbody):
        # get index, value from enumerate
        print(idx+1, stock[1])
        temp_stock_dict = extract_stock_detail_dict(stock[-1])  # 테스트시 여기에 stock_number 넣어보면 됨 = insert test stock_number
        
        if check_low_stock(stock, temp_stock_dict["year_financial"]):
            if check_low_stock(stock, temp_stock_dict["quarter_financial"]):
                low_stocks_list.append(stock)
            else:
                print("[Not Accept]\n")
        else:
                print("[Not Accept]\n")

    return low_stocks_list


def extract_low_value_stock(stock_kind_num):
    if stock_kind_num == 0:
        stock_kind_name = "KOSPI"
        STOCK_LIST_URL = KOSPI_STOCK_LIST_URL
        capi_standard = KOSPI_CAPITALIZATION_STANDARD
        FNAME_CAPI_OVER_STANDARD_STOCKS = f"capi_over_{capi_standard}_stocks"
        max_page_num = KOSPI_MAX_PAGE_NUM

    elif stock_kind_num == 1:
        stock_kind_name = "KOSDAQ"
        STOCK_LIST_URL = KOSDAQ_STOCK_LIST_URL
        capi_standard = KOSDAQ_CAPITALIZATION_STANDARD
        FNAME_CAPI_OVER_STANDARD_STOCKS = f"capi_over_{capi_standard}_stocks"
        max_page_num = KOSDAQ_MAX_PAGE_NUM

    else:
        print("Error: extract_stock_capitalization_rank")
        return False
    
    stocks_capi_rank = extract_stock_capitalization_rank(STOCK_LIST_URL, max_page_num)
    save_list_to_file(f"{CSV_FORDER}/{TODAY}_{stock_kind_name}_{FNAME_CAPITALIZATION_RANK}.{FILE_FORMAT}", stocks_capi_rank)

    stocks_capi_over_rank = extract_over_capi_standard_stocks(stocks_capi_rank, capi_standard)
    save_list_to_file(f"{CSV_FORDER}/{TODAY}_{stock_kind_name}_{FNAME_CAPI_OVER_STANDARD_STOCKS}.{FILE_FORMAT}", stocks_capi_over_rank)

    stocks_accept_PER_ROE = extract_accept_PER_ROE_list(stocks_capi_over_rank)
    save_list_to_file(f"{CSV_FORDER}/{TODAY}_{stock_kind_name}_{FNAME_ACCEPTED_PER_ROE_LIST}.{FILE_FORMAT}", stocks_accept_PER_ROE)

    stocks_accepted_low_value = extract_accepted_low_value_stocks(stocks_accept_PER_ROE)
    save_list_to_file(f"{CSV_FORDER}/{TODAY}_{stock_kind_name}_{FNAME_LOW_VALUATION_LIST}.{FILE_FORMAT}", stocks_accepted_low_value)

# Extract!
extract_low_value_stock(KOSPI)
extract_low_value_stock(KOSDAQ)
