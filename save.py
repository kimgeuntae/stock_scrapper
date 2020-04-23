# -*- coding: utf-8 -*-
import csv

def save_to_file(stocks):

    file = open("capitalization_rank.csv", mode="w", encoding="utf-8", newline="")  # encoding - 한글깨짐 , newline - 개행 삭제
    writer = csv.writer(file)
    
    for stock in stocks:
        writer.writerow(stock)
    return 
