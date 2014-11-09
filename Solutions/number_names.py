#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Number Names - Show how to spell out a number in English. You can use a preexisting implementation or roll your own, but you should support inputs up to at least one million (or the maximum value of your language's default bounded integer type, if that's less). Optional: Support for inputs other than positive integers (like zero, negative integers, and floating-point numbers).

Part of code by : Christopher Scott
http://www.scottdchris.com/
"""

number_user = \
    int(raw_input('Please enter the number you would like to spell out. >> '
        ))

units = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    ]
teens = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
    ]
tens = [
    '',
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
    ]


# Takes the number, and divides each section of the number to place it into an array.

def numToArray(num):
    numArray = [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        ]
    numArray[0] = num / 100000000 % 10  # Hundred Millions place
    numArray[1] = num / 10000000 % 10  # Ten Millions place
    numArray[2] = num / 1000000 % 10  # Millions place
    numArray[3] = num / 100000 % 10  # Hundred-thousands place
    numArray[4] = num / 10000 % 10  # Ten-thousands place
    numArray[5] = num / 1000 % 10  # Thousands place
    numArray[6] = num / 100 % 10  # Hundreds place
    numArray[7] = num / 10 % 10  # Tens place
    numArray[8] = num / 1 % 10  # Ones place
    return numArray


def hasTrailingZeros(numArray):
    if numArray[6] != 0:
        return numArray[7] == 0 and numArray[8] == 0
    elif numArray[3] != 0 or numArray[4] != 0 or numArray[5] != 0:
        return numArray[6] == 0 and numArray[7] == 0 and numArray[8] \
            == 0
    elif numArray[0] != 0 or numArray[1] != 0 or numArray[2] != 0:
        return numArray[3] == 0 and numArray[4] == 0 and numArray[5] \
            == 0 and numArray[6] == 0 and numArray[7] == 0 \
            and numArray[8] == 0


def numToWords(num):
    numArray = numToArray(num)
    word = ''
    if num == 0:
        word = 'zero'
    if num >= 1 and num <= 9:
        word = units[num]
    if num >= 10 and num <= 19:
        word = teens[num % 10]
    if num >= 20 and num <= 99:
        word += tens[num / 10]
        if numArray[8] != 0:
            word += ' ' + units[num % 10]

    if num >= 100 and num <= 999:
        word += units[numArray[6]] + ' hundred '
        if not hasTrailingZeros(numArray):
            word += numToWords(numArray[7] * 10 + numArray[8])

    if num >= 1000 and num <= 999999:
        word += numToWords(numArray[3] * 100 + numArray[4] * 10
                           + numArray[5]) + ' thousand '
        if not hasTrailingZeros(numArray):
            word += numToWords(numArray[6] * 100 + numArray[7] * 10
                               + numArray[8])

    if num >= 1000000 and num <= 999999999:
        word += numToWords(numArray[0] * 100 + numArray[1] * 10
                           + numArray[2]) + ' million '
        if not hasTrailingZeros(numArray):
            word += numToWords(numArray[3] * 100000 + numArray[4]
                               * 10000 + numArray[5] * 1000
                               + numArray[6] * 100 + numArray[7] * 10
                               + numArray[8])

    word = ' '.join(word.split())
    return word


def spell_number():
    print 'In words, the number is spelled :\t%s' \
        % numToWords(number_user)


spell_number()
