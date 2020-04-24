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




