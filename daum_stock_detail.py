import requests
from bs4 import BeautifulSoup

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
        
    result = requests.get(STATE_FINANCIAL_STATEMENT_DETAIL_URL)
    soup = BeautifulSoup(result.text, "html.parser")

    print(soup.find_all("script"))
    
    return "a"