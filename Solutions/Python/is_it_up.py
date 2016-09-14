#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
**Site Checker with Time Scheduling** - An application that attempts to connect to a website or server every so many minutes or a given time and check if it is up. If it is down, it will notify you by email or by posting a notice on screen.
"""


import os,time
print("Look up every hour if a site is up.")
hostname = raw_input("Please enter the website you want to look up in the derp.com format. >> ") #example
response = os.system("ping -c 1 " + hostname)

while True:
    if response == 0:
      print hostname, 'is up!'
    else:
      print hostname, 'is down!'
    time.sleep(3600)
