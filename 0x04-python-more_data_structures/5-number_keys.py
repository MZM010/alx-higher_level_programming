#!/usr/bin/python3
def number_keys(a_dictionary):
    counter = 0
    list_dict = list(a_dictionary)
    for i in range(len(list_dict)):
        counter += i
    return int(counter)
