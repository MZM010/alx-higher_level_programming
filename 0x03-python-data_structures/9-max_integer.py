#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    Max = 0
    if not isinstance(my_list, list):
        return None
    else:
        for item in my_list:
            if not isinstance(item, int):
                return None
            elif item > Max:
                Max = item
    return Max
