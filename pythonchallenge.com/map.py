#!/usr/bin/env python2
#http://www.pythonchallenge.com/pc/def/map.html

def decode(enc):
    dec = ''
    for c in enc:
        if ord(c) < ord("a"):
            dec += c
            continue
        c = ord(c)+2
        if c > ord("z"):
            c = c-ord("z")+ord("a")-1
        dec += chr(c)
    return dec

enc = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print decode(enc)
print 'http://pythonchallenge.com/pc/def/' + decode("map") + '.html'

