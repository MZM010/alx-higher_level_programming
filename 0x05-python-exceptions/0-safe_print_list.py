#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    total = 0
    while i < x:
        try:
            total = (total * 10) + my_list[i]
            i += 1
        except IndexError:
            break
    print("{}".format(total))
    return i
