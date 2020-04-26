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
    # simple_BPS = (total_amount_capital + capital) / total_stocks

    # profit
    total_amount_capital = stock_dict["total_amount_capital"]   # 자본 총계
    capital = stock_dict["capital"] # 자본금
    business_income = stock_dict["business_income"] # 영업이익
    current_net_income = stock_dict["current_net_income"]   # 당기순이익
    FCF = stock_dict["FCF"] # 투자금

    profit = total_amount_capital + capital + business_income + current_net_income + FCF

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

def get_debt_percent(stock_dict, debt_standard):
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

    debt_percent = get_part_percent(profit, deficit)
    
    if is_over(debt_percent, debt_standard):    # 부채비율이 기준비율보다 높은지
        return False    # 높으면 제외.
    else:
        return True