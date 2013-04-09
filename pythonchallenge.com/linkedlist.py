#!/usr/bin/env python2
import urllib


next = "12345"
next = "37085"
next = "46059"
for i in range(1,300):
    page = urllib.urlopen("http://pythonchallenge.com/pc/def/linkedlist.php?nothing=" + next ).read()
    next = page.split()[len(page.split())-1]
    print page

