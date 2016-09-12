#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import sleep
"""
Happy Numbers - A happy number is defined by the following process. Starting
with any positive integer, replace the number by the sum of the squares of its
digits, and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for
which this process ends in 1 are happy numbers, while those that do not end in
1 are unhappy numbers. Display an example of your output here. Find first 8
happy numbers.
"""

def happy_number(number):
    original_number = number
    known_numbers = []
    while number > 1 and number not in known_numbers:
        known_numbers.append(number)
        number_list = list(str(number))
        # Reset number to 0 to prevent adding the old number to the new list of
        # square numbers.
        number = 0
        for i in number_list:
            number += int(i) ** 2
        #print(known_numbers)
        #sleep(1)

    if number in known_numbers:
        print(str(original_number) + " is not a happy number. ")
    elif number == 1:
        print("Found a happy number ! >> " + str(original_number))

def main():
    choice = int(input("Would you like to find all numbers from 0 to 100 or test a specific number ? >> \n 1 -> Specific number\n 2 -> A range of numbers.\n>> "))
    if choice == 1:
        user_input = 0
        while user_input < 1:
            user_input = int(input("Please enter a positive number. >> "))
        happy_number(user_input)
    elif choice == 2:
        start = int(input("Please enter a number from 1 to x. >> "))
        finish = int(input("Please enter a number from 2 to x. >>"))
        for i in range(start , finish):
            happy_number(i)
    else:
        exit

if __name__ == '__main__':
    main()
