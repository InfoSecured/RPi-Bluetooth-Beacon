#/usr/bin/env python

import time
import bluetooth
import requests

home = 0

while True:
    print "Checking" + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
    result = bluetooth.lookup_name('Insert MAC Address Here', timeout=5)
    if (result != None):
        print "User present"
        if (home == 0):
            res = requests.post('Insert HTTPS Post Here', data='')
            print res
            home = 1
            print home
            time.sleep(600)
    else:
        print "User out of range"
        if (home == 1):
            res = requests.post('Insert HTTPS Post Here', data='')
            print res
            home = 0
            print home
            time.sleep(600)
    time.sleep(10)
