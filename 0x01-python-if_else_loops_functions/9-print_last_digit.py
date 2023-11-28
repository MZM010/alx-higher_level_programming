#!/usr/bin/python3
def print_last_digit(number):
    return print("{}".format(int(abs(number)) % 10), end="")
