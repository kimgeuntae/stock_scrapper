import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from stock_evaluation import is_True

def extract_stock_detail_dict(stock_number):
    # STOCK_DETAIL_URL = f"https://finance.daum.net/quotes/A{stock_number}#analysis/main"

    if is_company(stock_number):
        stock_dict = extract_state_financial_statement_detail(stock_number)
        return stock_dict
    else:
        return False
    

# check stock is company
def is_company(stock_number):
    STOCK_DETAIL_TOTAL_URL = f"https://wisefn.finance.daum.net/v1/company/c1010001.aspx?cmp_cd={stock_number}"
    # ETF_DETAIL_TOTAL_URL = f"https://wisefn.finance.daum.net/v1/ETF/index.aspx?cmp_cd={stock_number}"
    
    result = requests.get(STOCK_DETAIL_TOTAL_URL)
    soup = BeautifulSoup(result.text, "html.parser")

    title_str = soup.find("title").string

    return is_True(title_str.find("기업모니터"))


# extract state_financial_statement
def extract_state_financial_statement_detail(stock_number):
    STATE_FINANCIAL_STATEMENT_DETAIL_URL = f"https://wisefn.finance.daum.net/v1/company/cF1001.aspx?cmp_cd={stock_number}&finGubun=MAIN"
    
    # selenium
    driver_path = "./chrome_driver/chromedriver"
    browser = webdriver.Chrome(driver_path)
    browser.get(STATE_FINANCIAL_STATEMENT_DETAIL_URL)
    time.sleep(1)

    html = browser.page_source

    soup = BeautifulSoup(html, "html.parser")
    browser.quit()

    table = soup.find("table")
    tbody = table.find("tbody")

    # get finance division , year, quarter
    finance_div = tbody.find("tr", {"class": "row0"}).find_all("th", {"scope": "colgroup"})
    yaer_line = int(finance_div[0]["colspan"])
    quarter_line = int(finance_div[1]["colspan"])

    
    # 가로줄 데이터 dict, 1부터 year+quarter 개수 합까지
    for i in range(1, yaer_line + quarter_line + 1):
        f"finance_dict{i}" = {}

        # 해야할일!!!
        # 가로 개수만큼 dict 를 만들거고, 거기에 세로 만큼 하나씩 dict 데이터를 넣을거임.
        # 그리고 완성된 dict 한개씩 list 에 append 할 예정.
        # 최종 list 에는 yaer_line + quarter_line 개수 만큼 리스트가 있고, 각 가로당 세로줄 데이터 dict 가 들어가게 됨.

        if i == 1:
            f"finance_dict{i}"
        

        temp_list = []

        for j in range(1, 35):

            tr = tbody.find("tr", {"class": f"row{j}"})
            ths = tr.find_all("th")

            for th in ths:
            
        

    

    
    return "a"