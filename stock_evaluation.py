# -*- coding: utf-8 -*-

def is_True(data):
    if data:
        return True
    else:
        return False

def append_from_list_to_list(from_list, to_list):
    for data in from_list:
        to_list.append(data)
    return to_list

def is_over(type_data, type_standard):
    if is_digit(type_data) and is_digit(type_standard) :
        if float(type_data) >= float(type_standard):
            return True
        return False
    else:
        return False

def is_bigger(type_standard, type_data):
    return is_over(type_data, type_standard)

def is_under(type_data, type_standard):
    if is_digit(type_data) and is_digit(type_standard):
        if float(type_data) <= float(type_standard):
            return True
        return False
    else:
        return False

def is_lower(type_standard, type_data):
    return is_under(type_data, type_standard)

def is_digit(str):
    try:
        tmp = float(str)
        return True
    except ValueError:
        return False

def is_near_percent(percent, standard_num, new_num):
    temp_num = standard_num - new_num
    temp_percent = new_num / temp_num * 100

    if percent > temp_percent:
        return True
    return False

def get_part_percent(standard_num, part_num):
    part_percent = part_num / standard_num * 100
    return part_percent

# EPS : 주당 순수익 - 클 수록 좋음 bigger better
def get_EPS(current_net_income, total_stocks):
    eps = current_net_income / total_stocks
    return eps

# PER : 주가 수익비율 - 낮을 수록 저평가 lower better
def get_PER(stock_price, eps):
    per = stock_price / eps
    return per

# BPS : 주당 순자산 - 클 수록 좋음 bigger better
def get_BPS(stock_dict):
    # public_BPS = stock_dict["BPS"]
    # simple_BPS = (total_capital + capital) / total_stocks

    # profit
    total_capital = stock_dict["total_capital"]   # 자본총계
    capital = stock_dict["capital"] # 자본금
    business_income = stock_dict["business_income"] # 영업이익
    current_net_income = stock_dict["current_net_income"]   # 당기순이익
    FCF = stock_dict["FCF"] # 투자금

    profit = total_capital + capital + business_income + current_net_income + FCF

    # deficit
    CFO = stock_dict["CFO"] # 영업활동현금흐름
    CFI = stock_dict["CFI"] # 투자활동현금흐름
    CFF = stock_dict["CFF"] # 재무활동현금흐름
    CAPEX = stock_dict["CAPEX"] # 추가 여부 결정 아직
    interest_debt = stock_dict["interest_debt"] # 이자발생부채
    
    deficit = CFO + CFI + CFF + CAPEX + interest_debt

    # total_stocks
    total_stocks = stock_dict["total_stocks"]   # 총 주식수

    calc_BPS = (profit - deficit) / total_stocks

    return calc_BPS

# PBR : 주가 순자산비율 - 1 미만 저평가(주가보다 순자산이 많음), 1 초과 고평가(주가보다 순자산이 적음) lower than 1 better
def get_PBR(stock_price, BPS):
    calc_PBR = stock_price / BPS
    return calc_PBR

# 부채비율
def get_debt_ratio(stock_dict, debt_standard):
    # profit
    total_assets = stock_dict["total_assets"]  # 자산총계
    capital = stock_dict["capital"]  # 자본금
    FCF = stock_dict["FCF"] # 투자금
    
    profit = total_assets + capital + FCF

    # deficit
    total_debt = stock_dict["total_debt"] # 부채총계
    CAPEX = stock_dict["CAPEX"] # 추가 여부 결정 아직
    interest_debt = stock_dict["interest_debt"] # 이자발생부채

    deficit = total_debt + CAPEX + interest_debt

    debt_ratio = get_part_percent(profit, deficit)
    
    if is_over(debt_ratio, debt_standard):    # 부채비율이 기준비율보다 높은지
        return False    # 높으면 제외.
    else:
        return True

# 주가 매출 비율 - 1 미만시 주가보다 매출이 높음 lower than 1 better
def get_PSR(stock_dict):
    capitalization = stock_dict["capitalization"]  # 시가총액
    total_sales = stock_dict["total_sales"]    # 총 매출액

    PSR = capitalization / total_sales

    return PSR

# 기업 가치
def get_EV(stock_dict):
    capitalization = stock_dict["capitalization"]  # 시가총액
    net_debt = stock_dict["net_debt"]  # 순 차입금
    cash = stock_dict["cash"]  # 현금성자산
    
    EV = capitalization + (net_debt - cash)

    return EV

# 기업 실 가치 비교 - 높으면 고평가, 낮으면 저평가 lower better
def get_EV_div_EBITDA(stock_dict):
    EV = stock_dict["EV"]
    EBITDA = stock_dict["EBITDA"]

    return float(EV/EBITDA)

def check_low_stock(stock_list, stock_financial_dict_lists):
    stock_price = stock_list[2]    # 주가
    stock_capitalization = stock_list[6]  # 시가총액

    year_bigger = 0  # 연도
    quarter_bigger = 0 # 분기
    sales_bigger = 0 # 매출액
    business_profits_bigger = 0  # 영업이익
    announced_business_profits_bigger = 0 # 영업이익(발표기준)
    pre_tax_business_profits_bigger = 0  # 세전계속사업이익
    net_income_bigger = 0  # 당기순이익
    ruled_net_income_bigger = 0  # 당기순이익(지배)
    not_ruled_net_income_lower = 0  # 당기순이익(비지배), 당기순이익의 3%이하.
    total_assets_bigger = 0  # 자산총계
    total_debt_lower = 0  # 부채총계
    total_capital_bigger = 0  # 자본총계
    ruled_total_capital_bigger = 0  # 자본총계(지배)
    not_ruled_total_capital_lower = 0  # 자본총계(비지배)
    capital_bigger = 0  # 자본금
    CFO_bigger_than_0 = 0  # 영업활동현금흐름 = 플러스면 영업 소득, 마이너스면 영업 손실
    CFI_lower_than_0 = 0  # 투자활동현금흐름 = 마이너스이면 투자하는 것. 최대 CFO 의 50% 를 넘기지는 말자.
    CFF_lower_than_0 = 0  # 재무활동현금흐름 = 플러스면 은행 대출, 마이너스면 은행 빛 갚거나 주주 배당.
    CAPEX_lower = 0  # CAPEX = 자본적지출, 투자, 개발, 토지 등 기업이 사용한 금액.
    FCF_bigger = 0  # FCF = 잉여현금흐름, 기업이 사용후 남은 돈.
    interest_debt_lower = 0  # 이자발생부채
    operating_profits_ratio_bigger = 0  # 영업이익률
    net_profit_ratio_bigger = 0  # 순이익률
    ROE_bigger = 5  # ROE
    ROA_bigger = 0  # ROA
    debt_ratio_lower = 130  # 부채비율
    capital_reserve_ratio_bigger = 0  # 자본유보율
    EPS_bigger = 0  # EPS
    PER_lower = 10  # PER
    BPS_bigger = stock_price  # BPS = bigger_than_stock_price
    PBR_lower_than_1 = 1  # PBR
    cash_DPS_better_big = 0  # 현금DPS = 주당 배당금
    cash_dividend_yield_ratio_bigger = 0  # 현금배당수익률
    cash_dividend_payout_ratio_bigger = 0  # 현금배당성향
    total_stocks = stock_list[7]  # 발행주식수(보통주) = 총 주식수
    
    for stock_financial_dict in stock_financial_dict_lists:
        # check date
        if year_bigger <= float(stock_financial_dict.get("year")):
            year_bigger = float(stock_financial_dict.get("year"))
        elif quarter_bigger <= float(stock_financial_dict.get("quarter")):
            quarter_bigger = float(stock_financial_dict.get("quarter"))
        else:
            return False
        
        # check sales
        if is_bigger(sales_bigger, float(stock_financial_dict.get("sales"))):
            sales_bigger = float(stock_financial_dict.get("sales"))
        else:
            return False
        
        # check business_profits
        if is_bigger(business_profits_bigger, float(stock_financial_dict.get("business_profits"))):
            business_profits_bigger = float(stock_financial_dict.get("business_profits"))
        else:
            return False
        
        # check announced_business_profits
        if is_bigger(announced_business_profits_bigger, float(stock_financial_dict.get("announced_business_profits"))):
            announced_business_profits_bigger = float(stock_financial_dict.get("announced_business_profits"))
        else:
            return False

        # check pre_tax_business_profits
        if is_bigger(pre_tax_business_profits_bigger, float(stock_financial_dict.get("pre_tax_business_profits"))):
            pre_tax_business_profits_bigger = float(stock_financial_dict.get("pre_tax_business_profits"))
        else:
            return False

        # check net_income
        if is_bigger(net_income_bigger, float(stock_financial_dict.get("net_income"))):
            net_income_bigger = float(stock_financial_dict.get("net_income"))
        else:
            return False
            
        # check ruled_net_income
        if is_bigger(ruled_net_income_bigger, float(stock_financial_dict.get("ruled_net_income"))):
            ruled_net_income_bigger = float(stock_financial_dict.get("ruled_net_income"))
        else:
            return False

        # check not_ruled_net_income
        if not_ruled_net_income_lower == 0:
            not_ruled_net_income_lower = float(stock_financial_dict.get("net_income"))

        if is_lower(float(stock_financial_dict.get("not_ruled_net_income")), not_ruled_net_income_lower):
            not_ruled_net_income_lower = float(stock_financial_dict.get("not_ruled_net_income"))
        else:
            return False
        
        # check total_assets
        if is_bigger(total_assets_bigger, float(stock_financial_dict.get("total_assets"))):
            total_assets_bigger = float(stock_financial_dict.get("total_assets"))
        else:
            return False

        # check total_debt
        if total_debt_lower == 0:
            total_debt_lower = float(stock_financial_dict.get("total_capital"))

        if is_lower(float(stock_financial_dict.get("total_debt")), total_debt_lower):
            total_debt_lower = float(stock_financial_dict.get("total_debt"))
        else:
            return False

        # check total_capital
        if is_bigger(total_capital_bigger, float(stock_financial_dict.get("total_capital"))):
            total_capital_bigger = float(stock_financial_dict.get("total_capital"))
        else:
            return False
        
        # check ruled_total_capital
        if is_bigger(ruled_total_capital_bigger, float(stock_financial_dict.get("ruled_total_capital"))):
            ruled_total_capital_bigger = float(stock_financial_dict.get("ruled_total_capital"))
        else:
            return False
        
        # check not_ruled_total_capital
        if not_ruled_total_capital_lower == 0:
            not_ruled_total_capital_lower = float(stock_financial_dict.get("ruled_total_capital"))

        if is_lower(float(stock_financial_dict.get("not_ruled_total_capital")), not_ruled_total_capital_lower):
            not_ruled_total_capital_lower = float(stock_financial_dict.get("not_ruled_total_capital"))
        else:
            return False
        
        # check capital
        if is_bigger(capital_bigger, float(stock_financial_dict.get("capital"))):
            capital_bigger = float(stock_financial_dict.get("capital"))
        else:
            return False

        # check CFO
        if not(is_bigger(CFO_bigger_than_0, float(stock_financial_dict.get("CFO")))):
            return False

        # check CFI
        if not(is_lower(CFI_lower_than_0, float(stock_financial_dict.get("CFI")))):
            return False
        
        # check CFF
        if not(is_lower(CFF_lower_than_0, float(stock_financial_dict.get("CFF")))):
            return False

        # check CAPEX
        if CAPEX_lower == 0:
            CAPEX_lower = float(stock_financial_dict.get("FCF"))

        if is_lower(float(stock_financial_dict.get("CAPEX")), CAPEX_lower):
            CAPEX_lower = float(stock_financial_dict.get("CAPEX"))
        else:
            return False
        
        # check FCF
        if is_bigger(FCF_bigger, float(stock_financial_dict.get("FCF"))):
            FCF_bigger = float(stock_financial_dict.get("FCF"))
        else:
            return False
        
        # check interest_debt
        if interest_debt_lower == 0:
            interest_debt_lower = float(stock_financial_dict.get("CFO"))

        if is_lower(float(stock_financial_dict.get("interest_debt")), interest_debt_lower):
            interest_debt_lower = float(stock_financial_dict.get("interest_debt"))
        else:
            return False
        
        # check operating_profits_ratio
        if is_bigger(operating_profits_ratio_bigger, float(stock_financial_dict.get("operating_profits_ratio"))):
            operating_profits_ratio_bigger = float(stock_financial_dict.get("operating_profits_ratio"))
        else:
            return False
        
        # check net_profit_ratio
        if is_bigger(net_profit_ratio_bigger, float(stock_financial_dict.get("net_profit_ratio"))):
            net_profit_ratio_bigger = float(stock_financial_dict.get("net_profit_ratio"))
        else:
            return False
        
        # check ROE
        if is_bigger(ROE_bigger, float(stock_financial_dict.get("ROE"))):
            ROE_bigger = float(stock_financial_dict.get("ROE"))
        else:
            return False
        
        # check ROA
        if is_bigger(ROA_bigger, float(stock_financial_dict.get("ROA"))):
            ROA_bigger = float(stock_financial_dict.get("ROA"))
        else:
            return False
        
        # check debt_ratio
        if is_lower(float(stock_financial_dict.get("debt_ratio")), debt_ratio_lower):
            debt_ratio_lower = float(stock_financial_dict.get("debt_ratio"))
        else:
            return False
        
        # check capital_reserve_ratio
        if is_bigger(capital_reserve_ratio_bigger, float(stock_financial_dict.get("capital_reserve_ratio"))):
            capital_reserve_ratio_bigger = float(stock_financial_dict.get("capital_reserve_ratio"))
        else:
            return False
        
        # check EPS
        if is_bigger(EPS_bigger, float(stock_financial_dict.get("EPS"))):
            EPS_bigger = float(stock_financial_dict.get("EPS"))
        else:
            return False

        # check PER
        if is_lower(float(stock_financial_dict.get("PER")), PER_lower):
            PER_lower = float(stock_financial_dict.get("PER"))
        else:
            return False

        # check BPS
        if is_bigger(BPS_bigger, float(stock_financial_dict.get("BPS"))):
            BPS_bigger = float(stock_financial_dict.get("BPS"))
        else:
            return False

        # check PBR
        if not(is_lower(PBR_lower_than_1, float(stock_financial_dict.get("PBR")))):
            return False

        # check cash_DPS
        if is_bigger(cash_DPS_better_big, float(stock_financial_dict.get("cash_DPS"))):
            cash_DPS_better_big = float(stock_financial_dict.get("cash_DPS"))
        else:
            return False

        # check cash_dividend_yield_ratio
        if is_bigger(cash_dividend_yield_ratio_bigger, float(stock_financial_dict.get("cash_dividend_yield_ratio"))):
            cash_dividend_yield_ratio_bigger = float(stock_financial_dict.get("cash_dividend_yield_ratio"))
        else:
            return False
        
        # check cash_dividend_payout_ratio
        if is_bigger(cash_dividend_payout_ratio_bigger, float(stock_financial_dict.get("cash_dividend_payout_ratio"))):
            cash_dividend_payout_ratio_bigger = float(stock_financial_dict.get("cash_dividend_payout_ratio"))
        else:
            return False

    return True
        
        
        
