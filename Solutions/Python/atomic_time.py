#!/usr/bin/python
# -*- coding: utf-8 -*-

# Get Atomic Time from Internet Clock -
# This program will get the true atomic time from an atomic time clock on the Internet.
# Use any one of the atomic clocks returned by a simple DuckDuckGo search.

# We use the europe.pool.ntp.org time. For that, we need a ntp request.

import ntplib
import time
import os
from time import ctime

# New NTP Client

time_request = ntplib.NTPClient()
os.system('clear')
while 1:
    try :
        response = time_request.request('europe.pool.ntp.org', version=3)
        print ctime(response.tx_time)
    except ntplib.NTPException, e: #In case NTP goes down, or your internet connexion is down.
        print(e)