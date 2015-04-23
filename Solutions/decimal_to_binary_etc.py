#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This program will do two things:
Take a decimal number, converter it to binary.
Take a binary number, convert it to decimal.

To do that, I need : 
A binary <-> decimal dictionnary.

From decimal to binary :
I split the number to a list, and for each number, I convert it to binary. #I need to read about binary, I think. I don't think that's how it's done.

From binary to decimal :
Find binary patterns, and convert them to binary.
"""

import os
import math


class user_menu(object):

    def start(self):
        os.system('clear')
        print '''Would you like to: 
1- Convert from binary to decimal
2- Convert from decimal to binary
'''

    def choice(self):
        user_choice = \
            int(raw_input('Please choose a options, 1 or 2. >>'))
        return user_choice

    def user_number_input(self, choice):
        while choice != 1 or choice != 2:
            if choice == 1:
                binary_numbers = []
                user_binary = \
                    raw_input('Please enter your binary number. >>')
                for number in user_binary:
                    binary_numbers.append(int(number))
                return binary_numbers
            elif choice == 2:
                user_decimal = \
                    int(raw_input('Please enter your decimal number. >>'
                        ))
                return user_decimal


class converter(object):

    def converter_to_binary(self, decimal_number):
        binary_list = []
        while decimal_number > 0.5:
            if decimal_number % 2 != 0:  # If a number/2 = a number and 1/2
                binary_list.append(1)
            else:
                binary_list.append(0)  # If a number is a whole number
            decimal_number /= 2  #  Divide the starting number by 2
            decimal_number = int(decimal_number)  # Get rid of the .5 if there is one.
        binary_result = binary_list[::-1]
        return binary_result

    def converter_to_decimal(self, binary_number_array):
        decimal_number = 0
        power = len(binary_number_array) - 1
        for item in binary_number_array:
            decimal_number += 2 ** power * item
            power -= 1
        return decimal_number


def main():
    startup = user_menu()
    startup.start()
    user_choice = startup.choice()
    user_number = startup.user_number_input(user_choice)

    print 'Converted, your number is :'
    conversion = converter()
    if user_choice == 1:
        print conversion.converter_to_decimal(user_number)
    elif user_choice == 2:
        print conversion.converter_to_binary(user_number)


if __name__ == '__main__':
    main()
