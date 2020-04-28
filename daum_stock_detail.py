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


# extract state financial statement
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

    # state financial statement table width titles
    titles_name = {
        1: "year",  # 연도
        2: "sales", # 매출액
        3: "business_profits",  # 영업이익
        4: "announced_business_profits", # 영업이익(발표기준)
        5: "pre_tax_business_profits",  # 세전계속사업이익
        6: "net_income",  # 당기순이익
        7: "ruled_net_income",  # 당기순이익(지배)
        8: "not_ruled_net_income",  # 당기순이익(비지배)
        9: "total_assets",  # 자산총계
        10: "total_debt",  # 부채총계
        11: "total_capital",  # 자본총계
        12: "ruled_total_capital",  # 자본총계(지배)
        13: "not_ruled_total_capital",  # 자본총계(비지배)
        14: "capital",  # 자본금
        15: "CFO",  # 영업활동현금흐름
        16: "CFI",  # 투자활동현금흐름
        17: "CFF",  # 재무활동현금흐름
        18: "CAPEX",  # CAPEX
        19: "FCF",  # FCF
        20: "interest_debt",  # 이자발생부채
        21: "operating_profits_ratio",  # 영업이익률
        22: "net_profit_ratio",  # 순이익률
        23: "ROE",  # ROE
        24: "ROA",  # ROA
        25: "debt_ratio",  # 부채비율
        26: "capital_reserve_ratio",  # 자본유보율
        27: "EPS",  # EPS
        28: "PER",  # PER
        29: "BPS",  # BPS
        30: "PBR",  # PBR
        31: "cash_DPS",  # 현금DPS - 주당 배당금
        32: "cash_dividend_yield_ratio",  # 현금배당수익률
        33: "cash_dividend_payout_ratio",  # 현금배당성향
        34: "total_stocks"  # 발행주식수(보통주) - 총 주식수 = *1000
    }

    # get finance division , year, quarter
    finance_div = tbody.find("tr", {"class": "row0"}).find_all("th", {"scope": "colgroup"})
    yaer_line = int(finance_div[0]["colspan"])
    quarter_line = int(finance_div[1]["colspan"])
   
    stock_dict = {}
    temp_year_list = []
    temp_quarter_list = []
    
    # 가로줄 데이터 dict, 1부터 year+quarter 개수 합까지
    for i in range(1, yaer_line + quarter_line + 1):
        finance_dict = {}

        # 가로줄당 세로줄 데이터 1~34까지 추출
        for j in range(1, 35):
            tr = tbody.find("tr", {"class": f"row{j}"})
            
            # th number = 1
            if j == 1:
                ths = tr.find_all("th")

                # year
                if i < 5:
                    finance_dict[titles_name[j]] = ths[i - 1].contents[0].split("/")[0]
                # quarter
                else:
                    finance_dict[titles_name[j]] = ths[i - 1].contents[0].split("/")[1]
                    
            else:
                tds = tr.find_all("td")
                finance_dict[titles_name[j]] = tds[i].string

        if i < 5:
            temp_year_list.append(finance_dict)
        else:
            temp_quarter_list.append(finance_dict)
    
    stock_dict["year_financial"] = temp_year_list
    stock_dict["quarter_financial"] = temp_quarter_list

    return stock_dict