def max_integer(my_list=[]):
    Max = 0
    for item in my_list:
        if item > Max:
            Max = item
    return Max
