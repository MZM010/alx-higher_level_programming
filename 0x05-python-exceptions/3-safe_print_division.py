#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result: {}".format(float(a / b)))
    except ZeroDivisionError:
        return None
    return float(a / b)
