# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def extract_stock_list_thead(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    all_stock_info = soup.find("div", {"class": "box_type_l"})  # stocks list - kospi , kosdaq - tab_style_1
    stock_table = all_stock_info.find("table", {"class": "type_2"})  # table list
    stock_thead = stock_table.find("thead").find_all("th")

    stock_thead_list = []

    # extract thead
    for name in stock_thead:
        stock_thead_list.append(name.string)

    return stock_thead_list[0:-1] # delete 토론실


def extract_stock_detail_url(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    all_stock_info = soup.find("div", {"class": "box_type_l"})  # stocks list - kospi , kosdaq - tab_style_1
    stock_table = all_stock_info.find("table", {"class": "type_2"})  # table list
    titles = stock_table.find_all("a", {"class": "tltle"})  # stock_name, stock_link

    stocks_detail_list = []

    # extract stocks_info
    for stock in titles:
        stocks_detail_list.append([stock.string, stock['href']])

    return stocks_detail_list


def extract_stock_list_tbody(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    all_stock_info = soup.find("div", {"class": "box_type_l"})  # stocks list - kospi , kosdaq - tab_style_1
    stock_table = all_stock_info.find("table", {"class": "type_2"})  # table list
    stock_tbody_tr = stock_table.find("tbody").find_all("tr")

    # stock_tb_navi = all_stock_info.find("table", {"class": "Nnavi"}) #navi list

    stocks_tbody = []

    stocks_no = []      # 순번
    stocks_name = []    # 종목명
    stocks_link = []    # 종목 링크
    stocks_price = []   # 현재가
    stocks_diff = []    # 전일비
    stocks_fluc = []    # 등락률
    stocks_par = []     # 액면가
    stocks_capi = []    # 시가총액
    stocks_total = []   # 상장 주식수
    stocks_foreign = [] # 외국인 비율
    stocks_volume = []  # 거래량
    stocks_PER = []     # PER
    stocks_ROE = []     # ROE

    # extract tbody
    for tr in stock_tbody_tr:
        NO = tr.find_all("td", {"class": "no"})
        TITLE = tr.find_all("a", {"class": "tltle"})
        NUMBER = tr.find_all("td", {"class": "number"})
        temp = []

        # num
        if NO:
            NUM = NO[0].string
            stocks_no.append(NUM)
            temp.append(NUM)

            # NAME
            NAME = TITLE[0].string  # 종목명
            stocks_name.append(NAME)
            temp.append(NAME)
            
            # URL
            HREF = TITLE[0]['href'] # 상세 URL
            stocks_link.append(HREF)
            # temp.append(HREF)

            # parse nubmer class
            PRICE = NUMBER[0].string  # 현재가
            stocks_price.append(PRICE)
            temp.append(PRICE)

            DIFF = NUMBER[1].find_all("span")[0].string.strip()  # 전일비
            stocks_diff.append(DIFF)
            temp.append(DIFF)

            FLUC = NUMBER[2].find_all("span")[0].string.strip()  # 등락률
            stocks_fluc.append(FLUC)
            temp.append(FLUC)

            PAR = NUMBER[3].string  # 액면가
            stocks_par.append(PAR)
            temp.append(PAR)

            CAPI = NUMBER[4].string  # 시가총액
            stocks_capi.append(CAPI)
            temp.append(CAPI)

            TOTAL = NUMBER[5].string  # 상장 주식수
            stocks_total.append(TOTAL)
            temp.append(TOTAL)

            FOREIGN = NUMBER[6].string  # 외국인 비율
            stocks_foreign.append(FOREIGN)
            temp.append(FOREIGN)

            VOLUME = NUMBER[7].string  # 거래량
            stocks_volume.append(VOLUME)
            temp.append(VOLUME)

            PER = NUMBER[8].string  # PER
            stocks_PER.append(PER)
            temp.append(PER)

            ROE = NUMBER[9].string  # ROE
            stocks_ROE.append(ROE)
            temp.append(ROE)

            stocks_tbody.append(temp)
    
    return stocks_tbody