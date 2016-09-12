#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Happy Numbers - A happy number is defined by the following process. Starting
with any positive integer, replace the number by the sum of the squares of its
digits, and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for
which this process ends in 1 are happy numbers, while those that do not end in
1 are unhappy numbers. Display an example of your output here. Find first 8
happy numbers.
"""

user_input = 0
while user_input < 1:
    user_input = int(input("Please enter a positive number. >> "))

def happy_number(number):
    while number > 1:
        print("Current number is >> " + str(number))
        number_list = list(str(number))
        # Reset number to 0 to prevent adding the old number to the new list of
        # square numbers.
        number = 0
        for i in number_list:
            print(i)
            number += int(i) ** 2
            print(number)
    print("Found a happy number ! >> " + str(number))


happy_number(user_input)
