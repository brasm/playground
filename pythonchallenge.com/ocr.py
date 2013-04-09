#!/usr/bin/env python2
#http://www.pythonchallenge.com/pc/def/ocr.html
def search(f):
    f = open(f,"r")
    s = f.read()
    f.close()
    result = ""
    for c in s:
        if ord(c) >= ord("a") and ord(c) <= ord("z"):
            result += c
    return result
print 'http://pythonchallenge.com/pc/def/' + search("data/ocr.txt") + '.html'
