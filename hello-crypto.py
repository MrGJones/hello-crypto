#!/usr/bin/env python

# hello crypto 
# crypo currency ticker sourced from bitstamp & displayed on pimoroni's Scroll pHAT HD
# made by @mrglennjones

import time
import signal
import unicodedata
import scrollphathd
from scrollphathd.fonts import font5x5

from time import sleep
import json
#import requests, json
import urllib

# choose currency to display
# Supported values for currency: btcusd, btceur, eurusd, xrpusd, xrpeur, xrpbtc, ltcusd, ltceur, ltcbtc, ethusd, etheur, ethbtc
currencies = ['btcusd','ethusd','ltcusd']

# put the chosen currency symbols here 
symbol = ['BTC','ETH','LTC']

#Uncomment to rotate the text
#scrollphathd.rotate(180)


while True:
    string = ''
    pos = 0
    for currency in currencies:

        url = 'https://www.bitstamp.net/api/v2/ticker/%s/' % currency
        #print(url)
        data = json.load(urllib.urlopen(url))
        print(data)
        
        string += '%s ' % symbol[pos]
        string += u'$%s' % data['last'] + '   '
        pos+=1
        
    for i in range(3):
        scrollphathd.clear()
        #print(string)
        buffer = scrollphathd.write_string(string, x=17, y=0, font=font5x5, brightness=0.2)        
        for c in range(buffer):
            scrollphathd.show()
            scrollphathd.scroll(1)
            time.sleep(0.05)

    sleep(20)
        
    

