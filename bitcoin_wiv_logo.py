#!/usr/bin/env python

from __future__ import division

import os
import sys
import time
#import signal
#import unicodedata
import scrollphathd
from scrollphathd.fonts import font5x5

from time import sleep
import json
import urllib

try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

BRIGHTNESS=0.2
IMAGE_FILE = "btclogo.png"
#IMAGE_FILE = "btc_logo_circle.png"
IMAGE_WIDTH = 17
IMAGE_HEIGHT = 17
URL = 'https://www.bitstamp.net/api/v2/ticker/btcusd/'

last = 0

while True:

    latest = float(json.load(urllib.urlopen(URL))['last'])
    #print(latest)
    
    scrollphathd.clear()

    if last == 0:
        # show startup logo
        scrollphathd.clear()
        scrollphathd.fill(0, 0, 0, IMAGE_WIDTH, IMAGE_HEIGHT + 14) 
        image_path = os.path.join(os.path.dirname(__file__), IMAGE_FILE)
        image = Image.open(image_path)
        pixels = image.load()


        for x in range(IMAGE_WIDTH):
            for y in range(IMAGE_HEIGHT):
                r,g,b = pixels[x,y]
                scrollphathd.pixel(x, y+7, (r/255) * BRIGHTNESS)

        scrollphathd.write_string('%s ' % int(latest), 1, IMAGE_HEIGHT+8, font5x5, 1, BRIGHTNESS)
        scrollphathd.scroll_to(0,0)

        for i in range(IMAGE_HEIGHT+8):
            scrollphathd.show()
            scrollphathd.scroll(0,1)
            time.sleep(0.05)

    else:
        scrollphathd.fill(0, 0, 0, 50, 14) # a nice big canvas to work with

        if latest > last:
            scrollphathd.scroll_to(0,0)
            scrollphathd.write_string('%s ' % int(last), 1, 1, font5x5, 1, BRIGHTNESS)
            scrollphathd.write_string('%s ' % int(latest), 1, 8, font5x5, 1, BRIGHTNESS)
            for c in range(8):
                scrollphathd.show()
                scrollphathd.scroll(0,1)
                time.sleep(0.05)

        if latest < last:
            scrollphathd.write_string('%s ' % int(latest), 1, 1, font5x5, 1, BRIGHTNESS)
            scrollphathd.write_string('%s ' % int(last), 1, 8, font5x5, 1, BRIGHTNESS)
            scrollphathd.scroll_to(0,-7)
            for c in range(8):
                scrollphathd.show()
                scrollphathd.scroll(0,-1)
                time.sleep(0.05)

        if latest == last:
            scrollphathd.scroll_to(0,0)
            scrollphathd.write_string('%s ' % int(latest), 1, 1, font5x5, 1, BRIGHTNESS)
            scrollphathd.write_string('%s ' % int(last), 24, 1, font5x5, 1, BRIGHTNESS)
            for c in range(24):
                scrollphathd.show()
                scrollphathd.scroll(1,0)
                time.sleep(0.015)
           

    last = latest
    
    sleep(5)
