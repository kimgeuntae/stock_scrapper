# -*- coding: utf-8 -*-

def is_over(type_data, type_standard):
    if float(type_data) >= float(type_standard):
        return True
    return False

def is_under(type_data, type_standard):
    if type_data < type_standard:
        return True
    return False


# over capi 3000
def is_safe_stock(capi):
    return is_over(capi, 3000)





