#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
PLEASE DO NOT USE THIS CODE FOR SECURE COMMUNICATION, IT IS FLAWED, UNSECURE AND IT DOESN'T WORK (FOR NOW)
IF YOU NEED TO TRANSMIST SECURE INFORMATION, PLEASE USE GPG (GPG.ORG)
"""
def letter_value(letter):
    dictionnary_letter = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
        ' ': 0,
        }
    value = dictionnary_letter[letter]
    return value


def number_letter(number):
    dictionnary_number = {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
        8: 'h',
        9: 'i',
        10: 'j',
        11: 'k',
        12: 'l',
        13: 'm',
        14: 'n',
        15: 'o',
        16: 'p',
        17: 'q',
        18: 'r',
        19: 's',
        20: 't',
        21: 'u',
        22: 'v',
        23: 'w',
        24: 'x',
        25: 'y',
        26: 'z',
        }
    value = dictionnary_number[number]
    return value


class crypto(object):

    def encrypt(self, text, key):
        text = list(text)
        key = list(key)
        result = []
        position_of_key = 0
        for letter in text:

            # Get the letter's value in the alphabet

            text_value = letter_value(letter)

            # Look at which position is the cursor on the key, get the value of that letter.

            if position_of_key == len(key):
                position_of_key = 0
                key_value = letter_value(key[position_of_key])
            else:
                key_value = letter_value(key[position_of_key])
            position_of_key += 1

            # Add both values, and get the letter that corresponds to that value.

            final_value = key_value + text_value
            while final_value > 26:
                final_value = final_value - 26
            result.append(number_letter(final_value))
        return result

    def decrypt(self, text, key):
        text = list(text)
        key = list(key)
        result = []
        position_of_key = 0
        for letter in text:

            # Get the letter's value in the alphabet

            text_value = letter_value(letter)

            # Look at which position is the cursor on the key, get the value of that letter.

            if position_of_key == len(key):
                position_of_key = 0
                key_value = letter_value(key[position_of_key])
            else:
                key_value = letter_value(key[position_of_key])
            position_of_key += 1

            # Add both values, and get the letter that corresponds to that value.

            final_value = key_value + text_value
            while final_value > 26:
                final_value = final_value - 26
            result.append(number_letter(final_value))
        return result


def main():
    i = crypto()
    user_choice = 0
    while user_choice != 1 and user_choice != 2:
        user_choice = \
            int(raw_input('''Would you like to:
1- Encrypt stuff ?
2- Decrypt stuff ?
>> '''))

    if user_choice == 1:
        user_text = raw_input('Please enter the text to encrypt. >> ')
        user_key = raw_input('Please enter the key for encryption. >> ')
        print i.encrypt(user_text.lower(), user_key.lower())
    elif user_choice == 2:
        user_text = raw_input('Please enter the text to decrypt. >> ')
        user_key = \
            raw_input('Pleas enter the key used for encryption. >> ')
        print i.decrypt(user_text, user_key)


if __name__ == '__main__':
    main()
