#!/usr/bin/env python2
#http://pythonchallenge.com/pc/def/peak.html

import urllib,pickle
url='http://www.pythonchallenge.com/pc/def/banner.p'
obj=pickle.load(urllib.urlopen(url))
for line in obj:
        print ''.join(map(lambda pair: pair[0]*pair[1], line))
