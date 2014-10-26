#!/usr/bin/python
# -*- coding: utf-8 -*-
# Mortgage Calculator -
# Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
# Also figure out how long it will take the user to pay back the loan.
total_to_pay = float(raw_input("Please enter how much you need to pay. >> "))
# This is in percent multiply it by 100.
intrest_rate = float(
    raw_input("Please enter your intrest rate per month in percent. >> "))
payed_by_month = float(
    raw_input("Please enter how much you want to pay per month. >> "))  # In Euros
month_needed = 0
total_payed = 0
import time

while 0 < total_to_pay:
    total_to_pay = total_to_pay * 1 + (intrest_rate / 100)
    total_to_pay = total_to_pay - payed_by_month
    month_needed = month_needed + 1
    print "-----------------------------------------------------------------"
    print " - Month", month_needed, "- resting to pay :", total_to_pay, " euros"

print '\nYou will need ', month_needed, ' months if you pay ', payed_by_month, ' at an intrest rate of ', intrest_rate, ' % per month.'
