#!/usr/bin/python3
def max_integer(my_list=[]):
    Max = 0
    if isinstance(my_list, list):
        for item in my_list:
            if item > Max:
                Max = item
    return Max
