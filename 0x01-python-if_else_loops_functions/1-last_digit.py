#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
the_absolute_value = abs(number)
the_last_digit = the_absolute_value % 10
if the_last_digit < 6 and the_last_digit != 0:
    if number < 0:
        print("Last digit of {} is -{} and is less than 6 and not 0"
              .format(number, the_last_digit))
    if number > 5:
        print("Last digit of {} is {} and is less than 6 and not 0"
              .format(number, the_last_digit))
elif number > 0 and the_last_digit > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, the_last_digit))
elif the_last_digit == 0:
    print("Last digit of {} is 0 and is 0".format(number))
