#!/usr/bin/python
# -*- coding: utf-8 -*-

# List of countrys plus TVA.

"""Tax Calculator -
Asks the user to enter a cost and either a country or state tax.
It then returns the tax plus the total cost with tax.
**Please note:**
This code is using the ISO_3166-1 Alpha-3 code for the international country codes.
https://en.wikipedia.org/wiki/ISO_3166-1 -- October 2014
"""

user_country = \
    str(raw_input('\nPlease enter the IOS_3166 Alpha-3 code for your country. >> '
        ))
user_price = \
    float(raw_input('\nPlease enter the price whithout taxe. >> '))
country = {
    'DZA': 17,
    'AGO': 10,
    'AND': 4.5,
    'ARG': 21,
    'ARM': 20,
    'AUS': 10,
    'AZE': 18,
    'BEN': 18,
    'BHS': 10,
    'BGD': 15,
    'BLR': 18,
    'BIH': 18,
    'CAN': 5,
    'CHN': 17,
    'COL': 16,
    'CIV': 18,
    'CYP': 19,
    'HRV': 18,
    'ECU': 12,
    'ISR': 18,
    'JPN': 18,
    'LBN': 10,
    'MKD': 18,
    'MLI': 18,
    'NZL': 12.5,
    'RUS': 18,
    'SEN': 18,
    'SRB': 18,
    'SGP': 18,
    'CHE': 8,
    'TUN': 18,
    'TUR': 18,
    'UKR': 20,
    'VEN': 15,
    'VNM': 10,
    'DEU': 19,
    'AUT': 20,
    'BEL': 21,
    'BGR': 20,
    'HVR': 25,
    'DNK': 25,
    'EST': 20,
    'ESP': 21,
    'FIN': 24,
    'FRA': 20,
    'GRC': 23,
    'HUN': 27,
    'IRL': 23,
    'ITA': 22,
    'LVA': 21,
    'LTU': 21,
    'LUX': 15,
    'MLT': 18,
    'NLD': 21,
    'POL': 23,
    'PRT': 23,
    'CZE': 21,
    'ROU': 24,
    'GBR': 20,
    'SVK': 20,
    'SVN': 22,
    'SWE': 25,
    }

if country[user_country]:
    print '---------------------------------------------'
    print 'Your country has a normal VTA of ', country[user_country], \
        '%.'
    taxe = float(country[user_country]) / 100 * user_price + user_price
    print '\nYour item will cost you,', taxe, 'with taxe.'
    print '---------------------------------------------'
else:
    print 'Lucky you, that country does not have a VTA. (Yet).'
