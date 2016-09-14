#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads."""

import random

nbr_user_flips = \
    int(input('Please enter the number of times you want the coin to flip. >> '
        ))
nbr_flips_total = 0
nbr_tails = 0
nbr_heads = 0

while nbr_flips_total < nbr_user_flips:
    if random.randint(0, 1) == 1:
        # print '\nThis coin gave tails.'
        nbr_tails += 1
        nbr_flips_total += 1
    elif random.randint(0, 1) == 0:
        # print '\nThis coin gave head. ;)'
        nbr_heads += 1
        nbr_flips_total += 1

print ('\nThis turn, heads came out', nbr_heads,
       ' times and tails came out', nbr_tails, ' times.')
