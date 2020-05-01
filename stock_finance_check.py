from stock_evaluation import *

def is_finance_fine(stock_list, stock_financial_dict_lists):

    # 매출액
    if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "sales", 30):
        return False
    
    # 영업이익
    if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "business_profits", 20):
        return False
    
    # # 영업이익(발표기준)
    # if not is_data_bigger_fine(stock_financial_dict_lists, "announced_business_profits"):
    #     return False
    
    # # 세전계속사업이익
    # if not is_data_bigger_than_num_fine(stock_financial_dict_lists, "pre_tax_business_profits", 1):
    #     return False
    
    # # 당기순이익
    # if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "net_income", 5):
    #     return False

    # # 당기순이익(지배)
    # if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "ruled_net_income", 10):
    #     return False
    
    # # 당기순이익(비지배)
    # if not is_data_lower_big_percent_fine(stock_financial_dict_lists, "not_ruled_net_income", 5):
    #     return False
    
    # # 자산총계
    # if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "total_assets", 10):
    #     return False
    
    # # 부채총계
    # if not is_data_lower_big_percent_fine(stock_financial_dict_lists, "total_debt", 5):
    #     return False
    
    # 자본총계
    if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "total_capital", 5):
        return False
    
    # # 자본총계(지배)
    # if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "ruled_total_capital", 10):
    #     return False
    
    # # 자본총계(비지배)
    # if not is_data_lower_big_percent_fine(stock_financial_dict_lists, "not_ruled_total_capital", 3):
    #     return False
    
    # # 자본금
    # if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "capital", 15):
    #     return False
    
    # 영업활동현금흐름
    if not is_data_bigger_than_num_fine(stock_financial_dict_lists, "CFO", 0):
        return False
    
    # 투자활동현금흐름
    if not is_data_lower_than_num_fine(stock_financial_dict_lists, "CFI", 0):
        return False
    
    # # 재무활동현금흐름
    # if not is_data_lower_than_num_fine(stock_financial_dict_lists, "CFF", 0):
    #     return False
    
    # # CAPEX = 자본적지출
    # if not is_data_lower_big_percent_fine(stock_financial_dict_lists, "CAPEX", 80):
    #     return False
    
    # # FCF = 잉여현금흐름
    # if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "FCF", 40):
    #     return False
    # elif not is_data_bigger_than_num_fine(stock_financial_dict_lists, "FCF", 0):
    #     return False
    
    # # 이자발생부채
    # if not is_data_lower_big_percent_fine(stock_financial_dict_lists, "interest_debt", 15):
    #     return False
    
    # # 영업이익률
    # if not is_data_bigger_fine(stock_financial_dict_lists, "operating_profits_ratio"):
    #     return False
    # elif not is_data_bigger_than_num_fine(stock_financial_dict_lists, "operating_profits_ratio", 15):
    #     return False
    
    # 순이익률
    if not is_data_bigger_fine(stock_financial_dict_lists, "net_profit_ratio"):
        return False
    elif not is_data_bigger_than_num_fine(stock_financial_dict_lists, "net_profit_ratio", 10):
        return False

    # ROE
    if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "ROE", 30):
        return False
    elif not is_data_bigger_than_num_fine(stock_financial_dict_lists, "ROE", 3):
        return False
    
    # ROA
    if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "ROA", 30):
        return False
    elif not is_data_bigger_than_num_fine(stock_financial_dict_lists, "ROA", 3):
        return False
    
    # 부채비율
    if not is_data_lower_big_percent_fine(stock_financial_dict_lists, "debt_ratio", 20):
        return False
    elif not is_data_lower_than_num_fine(stock_financial_dict_lists, "debt_ratio", 130):
        return False
    
    # # 자본유보율
    # if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "capital_reserve_ratio", 3):
    #     return False
    # elif not is_data_bigger_than_num_fine(stock_financial_dict_lists, "capital_reserve_ratio", 0):
    #     return False
    
    # # EPS
    # if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "EPS", 20):
    #     return False
    # elif not is_data_bigger_than_num_fine(stock_financial_dict_lists, "EPS", 0):
    #     return False
    
    # # PER
    # if not is_data_lower_big_percent_fine(stock_financial_dict_lists, "PER", 30):
    #     return False
    # elif not is_data_lower_than_num_fine(stock_financial_dict_lists, "PER", 10):
    #     return False
    
    # # BPS
    # if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "BPS", 10):
    #     return False
    # elif not is_data_bigger_than_num_fine(stock_financial_dict_lists, "BPS", 0):
    #     return False
    
    # # PBR
    # if not is_data_lower_than_num_fine(stock_financial_dict_lists, "PBR", 2):
    #     return False
    # elif not is_data_lower_fine(stock_financial_dict_lists, "PBR"):
    #     return False

    # 현금DPS = 주당 배당금
    if not is_data_bigger_fine(stock_financial_dict_lists, "cash_DPS"):
        return False
    
    # # 현금배당수익률
    # if not is_data_bigger_low_percent_fine(stock_financial_dict_lists, "cash_dividend_yield_ratio", 35):
    #     return False
    # elif not is_data_bigger_than_num_fine(stock_financial_dict_lists, "BPS", 0):
    #     return False
    
    # # 현금배당성향
    # if not is_data_bigger_fine(stock_financial_dict_lists, "cash_dividend_payout_ratio"):
    #     return False
    
    # # 발행주식수(보통주) = 총 주식수
    # if not is_data_lower_fine(stock_financial_dict_lists, ""):
    #     return False
    
    return True

def check_low_stock(stock_list, finance_dict_list):
    if not is_finance_fine(stock_list, finance_dict_list.get("year_financial")):
        return False

    if not is_finance_fine(stock_list, finance_dict_list.get("quarter_financial")):
        return False

    return True