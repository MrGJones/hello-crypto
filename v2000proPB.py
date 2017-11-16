#!/usr/bin/env python

import time
import signal
import unicodedata
import scrollphathd
from scrollphathd.fonts import font5x5

from time import sleep
import json
import urllib

url = 'https://www.bitstamp.net/api/v2/ticker/btcusd/'

BRIGHTNESS=0.2

last = 0

while True:

    latest = float(json.load(urllib.urlopen(url))['last'])
    print(latest)
    
    scrollphathd.clear()
    scrollphathd.fill(0, 0, 0, 50, 14) # a nice big canvas to work with

    if latest > last:
        scrollphathd.scroll_to(0,0)
        scrollphathd.write_string('%s ' % int(last), 0, 0, font5x5, 1, BRIGHTNESS)
        scrollphathd.write_string('%s ' % int(latest), 0, 7, font5x5, 1, BRIGHTNESS)
        for c in range(8):
            scrollphathd.show()
            scrollphathd.scroll(0,1)
            time.sleep(0.05)

    if latest < last:
        scrollphathd.write_string('%s ' % int(latest), 0, 0, font5x5, 1, BRIGHTNESS)
        scrollphathd.write_string('%s ' % int(last), 0, 7, font5x5, 1, BRIGHTNESS)
        scrollphathd.scroll_to(0,-7)
        for c in range(8):
            scrollphathd.show()
            scrollphathd.scroll(0,-1)
            time.sleep(0.05)

    if latest == last:
        scrollphathd.scroll_to(0,0)
        scrollphathd.write_string('%s ' % int(latest), 0, 0, font5x5, 1, BRIGHTNESS)
        scrollphathd.write_string('%s ' % int(last), 23, 0, font5x5, 1, BRIGHTNESS)
        for c in range(24):
            scrollphathd.show()
            scrollphathd.scroll(1,0)
            time.sleep(0.025)        # half the delay of the vertical scroll

    last = latest
    
    sleep(5)
