# -*- coding: utf-8 -*-

def append_from_list_to_list(from_list, to_list):
    for data in from_list:
        to_list.append(data)
    return to_list

def is_over(type_data, type_standard):
    if is_digit(type_data):
        if float(type_data) >= float(type_standard):
            return True
        return False

def is_under(type_data, type_standard):
    if is_digit(type_data):
        if float(type_data) <= float(type_standard):
            return True
        return False

def is_digit(str):
    try:
        tmp = float(str)
        return True
    except ValueError:
        return False


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
    public_BPS = stock_dict["BPS"]

    # profit
    total_amount_capital = stock_dict["total_amount_capital"]
    capital = stock_dict["capital"]
    business_income = stock_dict["business_income"]
    current_net_income = stock_dict["current_net_income"]
    FCF = stock_dict["FCF"]

    # deficit
    CFO = stock_dict["CFO"]
    CFI = stock_dict["CFI"]
    CFF = stock_dict["CFF"]
    CAPEX = stock_dict["CAPEX"]
    interest_debt = stock_dict["interest_debt"]

    total_stocks = stock_dict["total_stocks"]

    profit = total_amount_capital + capital + business_income + current_net_income + FCF
    deficit = CFO + CFI + CFF + CAPEX + interest_debt
    
    simple_BPS = (total_amount_capital + capital) / total_stocks

    calc_BPS = (profit - deficit) / total_stocks

