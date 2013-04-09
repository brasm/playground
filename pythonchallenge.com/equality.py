#!/usr/bin/env python2
#http://www.pythonchallenge.com/pc/def/equality.html
import string
def isMatch(s):
    if str.isupper(s[:3]) and str.islower(s[-1]):
        return True 
    return False

def search(f):
    f = open(f,"r")
    s = f.read()
    f.close()
    s = string.join(s.split(),'')
    result = ""
    i = 0
    guard = 0
    for c in s:
        if str.isupper(c):
            guard=guard+1
        else:
            if guard is 3 and isMatch(s[i+1:i+5]):
                result += c
            guard = 0
        i = i+1
    return result
print 'http://pythonchallenge.com/pc/def/' + search("data/equality.txt") + '.html'
