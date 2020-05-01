

# 연도
def is_year_fine(stock_financial_dict_lists):
    year_bigger = 0

    for stock_financial_dict in stock_financial_dict_lists:
        # check sales
        sales_bigger = is_financial_data_bigger_low_inner_percent(30, sales_bigger, float(stock_financial_dict.get("sales")))
        if is_boolean(sales_bigger):
            return False
    return True

# 분기
def is_quarter_fine(stock_financial_dict_lists):
    quarter_bigger = 0

    for stock_financial_dict in stock_financial_dict_lists:
        # check sales
        sales_bigger = is_financial_data_bigger_low_inner_percent(30, sales_bigger, float(stock_financial_dict.get("sales")))
        if is_boolean(sales_bigger):
            return False
    return True

# 매출액
def is_sales_fine(stock_financial_dict_lists):
    if not is_data_fine(stock_financial_dict_lists, "sales"):
        return False
    
    return True

# 영업이익
def is_business_profits_fine(stock_financial_dict_lists):
    business_profits_bigger = 0

    for stock_financial_dict in stock_financial_dict_lists:
        # check business_profits
        business_profits_bigger = is_financial_data_bigger_low_inner_percent(20, business_profits_bigger, float(stock_financial_dict.get("business_profits")))
        if is_boolean(business_profits_bigger):
            return False
    return True

# 영업이익(발표기준)
def is_announced_business_profits_fine(stock_financial_dict_lists):
    announced_business_profits_bigger = 0

    for stock_financial_dict in stock_financial_dict_lists:
        # check announced_business_profits
        announced_business_profits_bigger = is_financial_data_bigger(announced_business_profits_bigger, float(stock_financial_dict.get("announced_business_profits")))
        if is_boolean(announced_business_profits_bigger):
            return False
    return True

# 세전계속사업이익
def is_pre_tax_business_profits_profits_fine(stock_financial_dict_lists):
    pre_tax_business_profits_bigger_than_1 = 1

    for stock_financial_dict in stock_financial_dict_lists:
        # check pre_tax_business_profits
        if not(is_bigger(pre_tax_business_profits_bigger_than_1, float(stock_financial_dict.get("pre_tax_business_profits")))):
            return False
    return True

# 당기순이익
def is_net_income_fine(stock_financial_dict_lists):
    net_income_bigger = 0

    for stock_financial_dict in stock_financial_dict_lists:
        # check net_income
        net_income_bigger = is_financial_data_bigger_low_inner_percent(5, net_income_bigger, float(stock_financial_dict.get("net_income")))
        if is_boolean(net_income_bigger):
            return False
    return True

# 당기순이익(지배)
def is_ruled_net_income_fine(stock_financial_dict_lists):
    ruled_net_income_bigger = 0

    for stock_financial_dict in stock_financial_dict_lists:
        # check ruled_net_income
        ruled_net_income_bigger = is_financial_data_bigger_low_inner_percent(10, ruled_net_income_bigger, float(stock_financial_dict.get("ruled_net_income")))
        if is_boolean(ruled_net_income_bigger):
            return False
    return True

# 당기순이익(비지배)
def is_not_ruled_net_income_fine(stock_financial_dict_lists):
    not_ruled_net_income_lower = 0

    for stock_financial_dict in stock_financial_dict_lists:
        # check not_ruled_net_income
        not_ruled_net_income_lower = is_financial_data_lower_inner_percent(5, not_ruled_net_income_lower, float(stock_financial_dict.get("not_ruled_net_income")))
        if is_boolean(not_ruled_net_income_lower):
            return False
    return True

# 자산총계
def is_total_assets_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check total_assets
        total_assets_bigger = is_financial_data_bigger_low_inner_percent(10, total_assets_bigger, float(stock_financial_dict.get("total_assets")))
        if is_boolean(total_assets_bigger):
            return False
    return True

# 부채총계
def is_total_debt_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check total_debt
        total_debt_lower = is_financial_data_lower_inner_percent(5, total_debt_lower, float(stock_financial_dict.get("total_debt")))
        if is_boolean(total_debt_lower):
            return False
    return True

# 자본총계
def is_total_capital_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check total_capital
        total_capital_bigger = is_financial_data_bigger_low_inner_percent(5, total_capital_bigger, float(stock_financial_dict.get("total_capital")))
        if is_boolean(total_capital_bigger):
            return False
    return True

# 자본총계(지배)
def is_ruled_total_capital_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check ruled_total_capital
        if ruled_total_capital_bigger == 0:
            ruled_total_capital_bigger = float(stock_financial_dict.get("ruled_total_capital"))
        elif is_bigger(ruled_total_capital_bigger, float(stock_financial_dict.get("ruled_total_capital"))):
            ruled_total_capital_bigger = float(stock_financial_dict.get("ruled_total_capital"))
        # lower than next value 
        elif (is_inner_percent_next(5, ruled_total_capital_bigger, float(stock_financial_dict.get("ruled_total_capital")))
            and float(stock_financial_dict.get("ruled_total_capital")) > float(stock_financial_dict.get("not_ruled_total_capital"))):
            ruled_total_capital_bigger = float(stock_financial_dict.get("ruled_total_capital"))
        else:
            return False
    return True

# 자본총계(비지배)
def is_not_ruled_total_capital_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check not_ruled_total_capital
        if not_ruled_total_capital_lower == 0:
            not_ruled_total_capital_lower = float(stock_financial_dict.get("not_ruled_total_capital"))
        elif is_lower(float(stock_financial_dict.get("not_ruled_total_capital")), not_ruled_total_capital_lower):
            not_ruled_total_capital_lower = float(stock_financial_dict.get("not_ruled_total_capital"))
        # lower than total_capital 3percent
        elif is_inner_percent_next(3, float(stock_financial_dict.get("not_ruled_total_capital")), float(stock_financial_dict.get("total_capital"))):
            not_ruled_total_capital_lower = float(stock_financial_dict.get("not_ruled_total_capital"))
        else:
            return False
    return True

# 자본금
def is_capital_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check capital
        capital_bigger = is_financial_data_bigger_low_inner_percent(15, capital_bigger, float(stock_financial_dict.get("capital")))
        if is_boolean(capital_bigger):
            return False
    return True

# 영업활동현금흐름
def is_CFO_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check CFO
        if not(is_bigger(CFO_bigger_than_0, float(stock_financial_dict.get("CFO")))):
            return False
    return True

# 투자활동현금흐름
def is_CFI_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check CFI
        if not(is_lower(CFI_lower_than_0, float(stock_financial_dict.get("CFI")))):
            return False
    return True

# 재무활동현금흐름
def is_CFF_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
         # check CFF
        if not(is_lower(CFF_lower_than_0, float(stock_financial_dict.get("CFF")))):
            return False
    return True

# CAPEX = 자본적지출
def is_CAPEX_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check CAPEX
        CAPEX_lower = is_financial_data_lower_inner_percent(80, CAPEX_lower, float(stock_financial_dict.get("CAPEX")))
        if is_boolean(CAPEX_lower):
            return False
    return True

# FCF = 잉여현금흐름
def is_FCF_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check FCF
        if FCF_bigger == 0:
            FCF_bigger = float(stock_financial_dict.get("FCF"))
        elif is_bigger(FCF_bigger, float(stock_financial_dict.get("FCF"))):
            FCF_bigger = float(stock_financial_dict.get("FCF"))
        elif (is_inner_percent_next(40, FCF_bigger, float(stock_financial_dict.get("FCF")))
            or float(stock_financial_dict.get("FCF")) > 0):
            FCF_bigger = float(stock_financial_dict.get("FCF"))
        else:
            return False
    return True

# 이자발생부채
def is_interest_debt_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check interest_debt
        interest_debt_lower = is_financial_data_lower_inner_percent(15, interest_debt_lower, float(stock_financial_dict.get("interest_debt")))
        if is_boolean(interest_debt_lower):
            return False
    return True

# 영업이익률
def is_operating_profits_ratio_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check operating_profits_ratio
        if operating_profits_ratio_bigger == 0:
            operating_profits_ratio_bigger = float(stock_financial_dict.get("operating_profits_ratio"))
        elif is_bigger(operating_profits_ratio_bigger, float(stock_financial_dict.get("operating_profits_ratio"))):
            operating_profits_ratio_bigger = float(stock_financial_dict.get("operating_profits_ratio"))
        elif float(stock_financial_dict.get("operating_profits_ratio")) > 15:
            operating_profits_ratio_bigger = float(stock_financial_dict.get("operating_profits_ratio"))
        else:
            return False
    return True

# 순이익률
def is_net_profit_ratio_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check net_profit_ratio
        if net_profit_ratio_bigger == 0:
            net_profit_ratio_bigger = float(stock_financial_dict.get("net_profit_ratio"))
        elif is_bigger(net_profit_ratio_bigger, float(stock_financial_dict.get("net_profit_ratio"))):
            net_profit_ratio_bigger = float(stock_financial_dict.get("net_profit_ratio"))
        elif float(stock_financial_dict.get("net_profit_ratio")) > 10:
            net_profit_ratio_bigger = float(stock_financial_dict.get("net_profit_ratio"))
        else:
            return False
    return True

# ROE
def is_ROE_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check ROE
        if ROE_bigger == 0:
            ROE_bigger = float(stock_financial_dict.get("ROE"))
        elif is_bigger(ROE_bigger, float(stock_financial_dict.get("ROE"))):
            ROE_bigger = float(stock_financial_dict.get("ROE"))
        elif (is_inner_percent_next(30, ROE_bigger, float(stock_financial_dict.get("ROE")))
            or float(stock_financial_dict.get("ROE")) > 5):
            ROE_bigger = float(stock_financial_dict.get("ROE"))
        else:
            return False
    return True

# ROA
def is_ROA_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check ROA
        if ROA_bigger == 0:
            ROA_bigger = float(stock_financial_dict.get("ROA"))
        elif is_bigger(ROA_bigger, float(stock_financial_dict.get("ROA"))):
            ROA_bigger = float(stock_financial_dict.get("ROA"))
        elif (is_inner_percent_next(30, ROA_bigger, float(stock_financial_dict.get("ROA")))
            or float(stock_financial_dict.get("ROA")) > 3):
            ROA_bigger = float(stock_financial_dict.get("ROA"))
        else:
            return False
    return True

# 부채비율
def is_debt_ratio_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check debt_ratio
        if debt_ratio_lower == 0:
            debt_ratio_lower = float(stock_financial_dict.get("debt_ratio"))
        elif is_lower(float(stock_financial_dict.get("debt_ratio")), debt_ratio_lower):
            debt_ratio_lower = float(stock_financial_dict.get("debt_ratio"))
        elif (is_inner_percent_next(20, debt_ratio_lower, float(stock_financial_dict.get("debt_ratio")))
            and float(stock_financial_dict.get("debt_ratio")) < 120):
            debt_ratio_lower = float(stock_financial_dict.get("debt_ratio"))
        else:
            return False
    return True

# 자본유보율
def is_capital_reserve_ratio_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check capital_reserve_ratio
        if capital_reserve_ratio_bigger == 0:
            capital_reserve_ratio_bigger = float(stock_financial_dict.get("capital_reserve_ratio"))
        elif is_bigger(capital_reserve_ratio_bigger, float(stock_financial_dict.get("capital_reserve_ratio"))):
            capital_reserve_ratio_bigger = float(stock_financial_dict.get("capital_reserve_ratio"))
        elif (is_inner_percent_next(3, capital_reserve_ratio_bigger, float(stock_financial_dict.get("capital_reserve_ratio")))
            and float(stock_financial_dict.get("capital_reserve_ratio")) > 0):
            capital_reserve_ratio_bigger = float(stock_financial_dict.get("capital_reserve_ratio"))
        else:
            return False
    return True

# EPS
def is_EPS_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check EPS
        if EPS_bigger == 0:
            EPS_bigger = float(stock_financial_dict.get("EPS"))
        elif is_bigger(EPS_bigger, float(stock_financial_dict.get("EPS"))):
            EPS_bigger = float(stock_financial_dict.get("EPS"))
        elif (is_inner_percent_next(20, EPS_bigger, float(stock_financial_dict.get("EPS")))
            and float(stock_financial_dict.get("EPS")) > 0):
            EPS_bigger = float(stock_financial_dict.get("EPS"))
        else:
            return False
    return True

# PER
def is_PER_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check PER
        if PER_lower == 0:
            PER_lower = float(stock_financial_dict.get("PER"))
        elif is_lower(float(stock_financial_dict.get("PER")), PER_lower):
            PER_lower = float(stock_financial_dict.get("PER"))
        elif (is_inner_percent_next(30, PER_lower, float(stock_financial_dict.get("PER")))
            or float(stock_financial_dict.get("PER")) < 10):
            PER_lower = float(stock_financial_dict.get("PER"))
        else:
            return False
    return True

# BPS
def is_BPS_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check BPS
        if BPS_bigger == 0:
            BPS_bigger = float(stock_financial_dict.get("BPS"))
        elif is_bigger(BPS_bigger, float(stock_financial_dict.get("BPS"))):
            BPS_bigger = float(stock_financial_dict.get("BPS"))
        elif (is_inner_percent_next(10, BPS_bigger, float(stock_financial_dict.get("BPS")))
            and float(stock_financial_dict.get("BPS")) > 0):
            BPS_bigger = float(stock_financial_dict.get("BPS"))
        else:
            return False
    return True

# PBR
def is_PBR_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check PBR
        if PBR_lower_than_2 == 2:
            PBR_lower_than_2 = float(stock_financial_dict.get("PBR"))
        elif is_lower(float(stock_financial_dict.get("PBR")), PBR_lower_than_2):
            PBR_lower_than_2 = float(stock_financial_dict.get("PBR"))
        elif not(is_lower(2, float(stock_financial_dict.get("PBR")))):
            return False
    return True

# 현금DPS = 주당 배당금
def is_cash_DPS_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check cash_DPS
        if is_bigger(cash_DPS_better_big, float(stock_financial_dict.get("cash_DPS"))):
            cash_DPS_better_big = float(stock_financial_dict.get("cash_DPS"))
        else:
            return False
    return True

# 현금배당수익률
def is_cash_dividend_yield_ratio_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check cash_dividend_yield_ratio
        if is_bigger(cash_dividend_yield_ratio_bigger, float(stock_financial_dict.get("cash_dividend_yield_ratio"))):
            cash_dividend_yield_ratio_bigger = float(stock_financial_dict.get("cash_dividend_yield_ratio"))
        elif (is_inner_percent_next(35, cash_dividend_yield_ratio_bigger, float(stock_financial_dict.get("cash_dividend_yield_ratio")))
            and float(stock_financial_dict.get("cash_dividend_yield_ratio")) > 0):
            cash_dividend_yield_ratio_bigger = float(stock_financial_dict.get("cash_dividend_yield_ratio"))
        else:
            return False
    return True

# 현금배당성향
def is_cash_dividend_payout_ratio_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
        # check cash_dividend_payout_ratio
        if is_bigger(cash_dividend_payout_ratio_bigger, float(stock_financial_dict.get("cash_dividend_payout_ratio"))):
            cash_dividend_payout_ratio_bigger = float(stock_financial_dict.get("cash_dividend_payout_ratio"))
        else:
            return False
    return True

# 발행주식수(보통주) = 총 주식수
def is_total_stocks_fine(stock_financial_dict_lists):
    for stock_financial_dict in stock_financial_dict_lists:
    return True



def check_low_stock(stock_list, stock_financial_dict_lists):
    stock_price = stock_list[2]    # 주가
    stock_capitalization = stock_list[6]  # 시가총액

    year_bigger = 0  # 연도
    quarter_bigger = 0 # 분기
    sales_bigger = 0 # 매출액
    business_profits_bigger = 0  # 영업이익
    announced_business_profits_bigger = 0 # 영업이익(발표기준)
    pre_tax_business_profits_bigger_than_1 = 1  # 세전계속사업이익
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
    BPS_bigger = float(stock_price.replace(",", ""))  # BPS = bigger_than_stock_price
    PBR_lower_than_2 = 2  # PBR
    cash_DPS_better_big = 0  # 현금DPS = 주당 배당금
    cash_dividend_yield_ratio_bigger = 0  # 현금배당수익률
    cash_dividend_payout_ratio_bigger = 0  # 현금배당성향
    total_stocks = stock_list[7]  # 발행주식수(보통주) = 총 주식수
    
    for stock_financial_dict in stock_financial_dict_lists:
        # check date
        if 'year' in stock_financial_dict:
            year_bigger = float(stock_financial_dict.get("year"))
        elif 'quarter' in stock_financial_dict:
            quarter_bigger = float(stock_financial_dict.get("quarter"))
        else:
            return False
        
        # check sales
        sales_bigger = is_financial_data_bigger_low_inner_percent(30, sales_bigger, float(stock_financial_dict.get("sales")))
        if is_boolean(sales_bigger):
            return False
        
        # check business_profits
        business_profits_bigger = is_financial_data_bigger_low_inner_percent(20, business_profits_bigger, float(stock_financial_dict.get("business_profits")))
        if is_boolean(business_profits_bigger):
            return False
        
        # check announced_business_profits
        announced_business_profits_bigger = is_financial_data_bigger(announced_business_profits_bigger, float(stock_financial_dict.get("announced_business_profits")))
        if is_boolean(announced_business_profits_bigger):
            return False

        # check pre_tax_business_profits
        if not(is_bigger(pre_tax_business_profits_bigger_than_1, float(stock_financial_dict.get("pre_tax_business_profits")))):
            return False

        # check net_income
        net_income_bigger = is_financial_data_bigger_low_inner_percent(5, net_income_bigger, float(stock_financial_dict.get("net_income")))
        if is_boolean(net_income_bigger):
            return False
            
        # # check ruled_net_income
        # ruled_net_income_bigger = is_financial_data_bigger_low_inner_percent(10, ruled_net_income_bigger, float(stock_financial_dict.get("ruled_net_income")))
        # if is_boolean(ruled_net_income_bigger):
        #     return False
        
        # # check not_ruled_net_income
        # not_ruled_net_income_lower = is_financial_data_lower_inner_percent(5, not_ruled_net_income_lower, float(stock_financial_dict.get("not_ruled_net_income")))
        # if is_boolean(not_ruled_net_income_lower):
        #     return False
        
        # # check total_assets
        # total_assets_bigger = is_financial_data_bigger_low_inner_percent(10, total_assets_bigger, float(stock_financial_dict.get("total_assets")))
        # if is_boolean(total_assets_bigger):
        #     return False

        # # check total_debt
        # total_debt_lower = is_financial_data_lower_inner_percent(5, total_debt_lower, float(stock_financial_dict.get("total_debt")))
        # if is_boolean(total_debt_lower):
        #     return False

        # # check total_capital
        # total_capital_bigger = is_financial_data_bigger_low_inner_percent(5, total_capital_bigger, float(stock_financial_dict.get("total_capital")))
        # if is_boolean(total_capital_bigger):
        #     return False
        
        # # check ruled_total_capital
        # if ruled_total_capital_bigger == 0:
        #     ruled_total_capital_bigger = float(stock_financial_dict.get("ruled_total_capital"))
        # elif is_bigger(ruled_total_capital_bigger, float(stock_financial_dict.get("ruled_total_capital"))):
        #     ruled_total_capital_bigger = float(stock_financial_dict.get("ruled_total_capital"))
        # # lower than next value 
        # elif (is_inner_percent_next(5, ruled_total_capital_bigger, float(stock_financial_dict.get("ruled_total_capital")))
        #     and float(stock_financial_dict.get("ruled_total_capital")) > float(stock_financial_dict.get("not_ruled_total_capital"))):
        #     ruled_total_capital_bigger = float(stock_financial_dict.get("ruled_total_capital"))
        # else:
        #     return False
        
        # # check not_ruled_total_capital
        # if not_ruled_total_capital_lower == 0:
        #     not_ruled_total_capital_lower = float(stock_financial_dict.get("not_ruled_total_capital"))
        # elif is_lower(float(stock_financial_dict.get("not_ruled_total_capital")), not_ruled_total_capital_lower):
        #     not_ruled_total_capital_lower = float(stock_financial_dict.get("not_ruled_total_capital"))
        # # lower than total_capital 3percent
        # elif is_inner_percent_next(3, float(stock_financial_dict.get("not_ruled_total_capital")), float(stock_financial_dict.get("total_capital"))):
        #     not_ruled_total_capital_lower = float(stock_financial_dict.get("not_ruled_total_capital"))
        # else:
        #     return False
        
        # # check capital
        # capital_bigger = is_financial_data_bigger_low_inner_percent(15, capital_bigger, float(stock_financial_dict.get("capital")))
        # if is_boolean(capital_bigger):
        #     return False
        
        # # check CFO
        # if not(is_bigger(CFO_bigger_than_0, float(stock_financial_dict.get("CFO")))):
        #     return False

        # # check CFI
        # if not(is_lower(CFI_lower_than_0, float(stock_financial_dict.get("CFI")))):
        #     return False
        
        # # check CFF
        # if not(is_lower(CFF_lower_than_0, float(stock_financial_dict.get("CFF")))):
        #     return False

        # # check CAPEX
        # CAPEX_lower = is_financial_data_lower_inner_percent(80, CAPEX_lower, float(stock_financial_dict.get("CAPEX")))
        # if is_boolean(CAPEX_lower):
        #     return False

        # # check FCF
        # if FCF_bigger == 0:
        #     FCF_bigger = float(stock_financial_dict.get("FCF"))
        # elif is_bigger(FCF_bigger, float(stock_financial_dict.get("FCF"))):
        #     FCF_bigger = float(stock_financial_dict.get("FCF"))
        # elif (is_inner_percent_next(40, FCF_bigger, float(stock_financial_dict.get("FCF")))
        #     or float(stock_financial_dict.get("FCF")) > 0):
        #     FCF_bigger = float(stock_financial_dict.get("FCF"))
        # else:
        #     return False
        
        # # check interest_debt
        # interest_debt_lower = is_financial_data_lower_inner_percent(15, interest_debt_lower, float(stock_financial_dict.get("interest_debt")))
        # if is_boolean(interest_debt_lower):
        #     return False
        
        # # check operating_profits_ratio
        # if operating_profits_ratio_bigger == 0:
        #     operating_profits_ratio_bigger = float(stock_financial_dict.get("operating_profits_ratio"))
        # elif is_bigger(operating_profits_ratio_bigger, float(stock_financial_dict.get("operating_profits_ratio"))):
        #     operating_profits_ratio_bigger = float(stock_financial_dict.get("operating_profits_ratio"))
        # elif float(stock_financial_dict.get("operating_profits_ratio")) > 15:
        #     operating_profits_ratio_bigger = float(stock_financial_dict.get("operating_profits_ratio"))
        # else:
        #     return False
        
        # # check net_profit_ratio
        # if net_profit_ratio_bigger == 0:
        #     net_profit_ratio_bigger = float(stock_financial_dict.get("net_profit_ratio"))
        # elif is_bigger(net_profit_ratio_bigger, float(stock_financial_dict.get("net_profit_ratio"))):
        #     net_profit_ratio_bigger = float(stock_financial_dict.get("net_profit_ratio"))
        # elif float(stock_financial_dict.get("net_profit_ratio")) > 10:
        #     net_profit_ratio_bigger = float(stock_financial_dict.get("net_profit_ratio"))
        # else:
        #     return False
        
        # # check ROE
        # if ROE_bigger == 0:
        #     ROE_bigger = float(stock_financial_dict.get("ROE"))
        # elif is_bigger(ROE_bigger, float(stock_financial_dict.get("ROE"))):
        #     ROE_bigger = float(stock_financial_dict.get("ROE"))
        # elif (is_inner_percent_next(30, ROE_bigger, float(stock_financial_dict.get("ROE")))
        #     or float(stock_financial_dict.get("ROE")) > 5):
        #     ROE_bigger = float(stock_financial_dict.get("ROE"))
        # else:
        #     return False
        
        # # check ROA
        # if ROA_bigger == 0:
        #     ROA_bigger = float(stock_financial_dict.get("ROA"))
        # elif is_bigger(ROA_bigger, float(stock_financial_dict.get("ROA"))):
        #     ROA_bigger = float(stock_financial_dict.get("ROA"))
        # elif (is_inner_percent_next(30, ROA_bigger, float(stock_financial_dict.get("ROA")))
        #     or float(stock_financial_dict.get("ROA")) > 3):
        #     ROA_bigger = float(stock_financial_dict.get("ROA"))
        # else:
        #     return False
        
        # # check debt_ratio
        # if debt_ratio_lower == 0:
        #     debt_ratio_lower = float(stock_financial_dict.get("debt_ratio"))
        # elif is_lower(float(stock_financial_dict.get("debt_ratio")), debt_ratio_lower):
        #     debt_ratio_lower = float(stock_financial_dict.get("debt_ratio"))
        # elif (is_inner_percent_next(20, debt_ratio_lower, float(stock_financial_dict.get("debt_ratio")))
        #     and float(stock_financial_dict.get("debt_ratio")) < 120):
        #     debt_ratio_lower = float(stock_financial_dict.get("debt_ratio"))
        # else:
        #     return False
        
        # # check capital_reserve_ratio
        # if capital_reserve_ratio_bigger == 0:
        #     capital_reserve_ratio_bigger = float(stock_financial_dict.get("capital_reserve_ratio"))
        # elif is_bigger(capital_reserve_ratio_bigger, float(stock_financial_dict.get("capital_reserve_ratio"))):
        #     capital_reserve_ratio_bigger = float(stock_financial_dict.get("capital_reserve_ratio"))
        # elif (is_inner_percent_next(3, capital_reserve_ratio_bigger, float(stock_financial_dict.get("capital_reserve_ratio")))
        #     and float(stock_financial_dict.get("capital_reserve_ratio")) > 0):
        #     capital_reserve_ratio_bigger = float(stock_financial_dict.get("capital_reserve_ratio"))
        # else:
        #     return False
        
        # # check EPS
        # if EPS_bigger == 0:
        #     EPS_bigger = float(stock_financial_dict.get("EPS"))
        # elif is_bigger(EPS_bigger, float(stock_financial_dict.get("EPS"))):
        #     EPS_bigger = float(stock_financial_dict.get("EPS"))
        # elif (is_inner_percent_next(20, EPS_bigger, float(stock_financial_dict.get("EPS")))
        #     and float(stock_financial_dict.get("EPS")) > 0):
        #     EPS_bigger = float(stock_financial_dict.get("EPS"))
        # else:
        #     return False

        # # check PER
        # if PER_lower == 0:
        #     PER_lower = float(stock_financial_dict.get("PER"))
        # elif is_lower(float(stock_financial_dict.get("PER")), PER_lower):
        #     PER_lower = float(stock_financial_dict.get("PER"))
        # elif (is_inner_percent_next(30, PER_lower, float(stock_financial_dict.get("PER")))
        #     or float(stock_financial_dict.get("PER")) < 10):
        #     PER_lower = float(stock_financial_dict.get("PER"))
        # else:
        #     return False

        # # check BPS
        # if BPS_bigger == 0:
        #     BPS_bigger = float(stock_financial_dict.get("BPS"))
        # elif is_bigger(BPS_bigger, float(stock_financial_dict.get("BPS"))):
        #     BPS_bigger = float(stock_financial_dict.get("BPS"))
        # elif (is_inner_percent_next(10, BPS_bigger, float(stock_financial_dict.get("BPS")))
        #     and float(stock_financial_dict.get("BPS")) > 0):
        #     BPS_bigger = float(stock_financial_dict.get("BPS"))
        # else:
        #     return False

        # # check PBR
        # if PBR_lower_than_2 == 2:
        #     PBR_lower_than_2 = float(stock_financial_dict.get("PBR"))
        # elif is_lower(float(stock_financial_dict.get("PBR")), PBR_lower_than_2):
        #     PBR_lower_than_2 = float(stock_financial_dict.get("PBR"))
        # elif not(is_lower(2, float(stock_financial_dict.get("PBR")))):
        #     return False

        # # check cash_DPS
        # if is_bigger(cash_DPS_better_big, float(stock_financial_dict.get("cash_DPS"))):
        #     cash_DPS_better_big = float(stock_financial_dict.get("cash_DPS"))
        # else:
        #     return False

        # # check cash_dividend_yield_ratio
        # if is_bigger(cash_dividend_yield_ratio_bigger, float(stock_financial_dict.get("cash_dividend_yield_ratio"))):
        #     cash_dividend_yield_ratio_bigger = float(stock_financial_dict.get("cash_dividend_yield_ratio"))
        # elif (is_inner_percent_next(35, cash_dividend_yield_ratio_bigger, float(stock_financial_dict.get("cash_dividend_yield_ratio")))
        #     and float(stock_financial_dict.get("cash_dividend_yield_ratio")) > 0):
        #     cash_dividend_yield_ratio_bigger = float(stock_financial_dict.get("cash_dividend_yield_ratio"))
        # else:
        #     return False
        
        # # check cash_dividend_payout_ratio
        # if is_bigger(cash_dividend_payout_ratio_bigger, float(stock_financial_dict.get("cash_dividend_payout_ratio"))):
        #     cash_dividend_payout_ratio_bigger = float(stock_financial_dict.get("cash_dividend_payout_ratio"))
        # else:
        #     return False

    return True
        