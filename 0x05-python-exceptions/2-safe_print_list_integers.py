#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    total = 0
    try:
        while i < x:
            try:
                num = int(my_list[i])
                print("{:d}".format(num), end=' ')
                total += 1
            except TypeError:
                pass
            i += 1
    except IndexError:
        pass
    print()
    return total
