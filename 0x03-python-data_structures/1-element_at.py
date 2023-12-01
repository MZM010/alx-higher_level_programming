#!/usr/bin/python3
def element_at(my_list, idx):
    lenghth = len(my_list)
    if idx > (lenghth - 1) or idx < 0:
        return None
    else:
        return my_list[idx]
