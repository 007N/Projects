#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This program will do two things:
Take a decimal number, converter it to binary.
Take a binary number, convert it to decimal.
"""

class user_menu(object):

    def start(self):
        print '''Would you like to: 
1- Convert from binary to decimal
2- Convert from decimal to binary
'''
    
    # How do you want to convert ?
    def choice(self):
        user_choice = 0
        while user_choice != 1 and user_choice != 2:
            user_choice = \
                int(raw_input('Please choose an option, 1 or 2. >> '))
        return user_choice

    # Get your decimal or binary number
    def user_number_input(self, choice):
        while choice != 1 or choice != 2:
            if choice == 1:
                binary_numbers = []
                user_binary = \
                    raw_input('Please enter your binary number. >> ')
                for number in user_binary:
                    binary_numbers.append(int(number))
                return binary_numbers
            elif choice == 2:
                user_decimal = \
                    int(raw_input('Please enter your decimal number. >> '
                        ))
                return user_decimal


class converter(object):

    # Uses a simple way to convert to binary
    def converter_to_binary(self, decimal_number):
        # We will put the binary number into a list
        binary_list = [] 
        while decimal_number > 0.5:
            if decimal_number % 2 != 0:
                binary_list.append(1)
            else:
                binary_list.append(0) 
            decimal_number /= 2 
            decimal_number = int(decimal_number) 
        binary_result = binary_list[::-1]
        return binary_result

    # Simple way to convert to decimal
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
    
    # Make the conversion and print it out all at once.
    if user_choice == 1:
        print conversion.converter_to_decimal(user_number)
    elif user_choice == 2:
        print ''.join(map(str,
                      conversion.converter_to_binary(user_number)))


if __name__ == '__main__':
    main()
