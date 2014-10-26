# Get Atomic Time from Internet Clock -
# This program will get the true atomic time from an atomic time clock on the Internet.
# Use any one of the atomic clocks returned by a simple Google search.

# We use the europe.pool.ntp.org time. For that, we need a ntp request.
import ntplib
import time
import os
from time import ctime

# New NTP Client
time_request = ntplib.NTPClient()
os.system('clear')
while 1:
    response = time_request.request('europe.pool.ntp.org', version=3)
    print("=*=*=*=*=*=*=\n")
    print(ctime(response.tx_time))
    print("\n=*=*=*=*=*=*=")
    time.sleep(0.8)  # Don't sleep one sec, otherwise the clock is not in sync.
    os.system('clear')  # Works only under UNIX systems.
