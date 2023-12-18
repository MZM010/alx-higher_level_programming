#!/usr/bin/python3
def safe_print_division(a, b):
    value = 0
    try:
        value = a / b
        print("Inside result: {}".format(value))
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return None
    return float(a / b)
