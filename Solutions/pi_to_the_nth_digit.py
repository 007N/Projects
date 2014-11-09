#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import the math module

""""Find PI to the Nth Digit"""

import math

# Ask until where Pi should go

precision = int(raw_input('How far would you like to discover Pi ? >>'))

# Define limit.

while precision > 100:
    print "Sorry, but you're going too far..."
    precision = \
        int(raw_input('How far would you like to discover Pi ? >>'))
else:

    # This prints Pi passed as an argument of %.
    # *F give the Floating decimal format and precision is it's argument.
    # See https://docs.python.org/2/library/stdtypes.html#string-formatting .

    print '%.*F' % (precision, math.pi)
