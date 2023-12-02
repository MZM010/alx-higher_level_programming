#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    Max = 0
    if isinstance(my_list, list):
        for item in my_list:
            if isinstance(item, int):
                if item > Max:
                    Max = item
            else:
                return None
    else:
        return None
    return Max
