#!/usr/bin/env python2
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import math

def isPalindromic(n):
    for i in range(1,int(math.ceil(len(str(n))/2)+2)):
        if str(n)[i-1] != str(n)[-(i)]:
            return False
    return True

def integralroots(n):
    init = math.sqrt(n)
    a = int(init)
    b = int(init)
    while True:
        calc = a*b
        if calc == n: return (a,b)
        if calc > n:
            b -= 1
        else:
            a += 1
        if b < 100 or a > 999:
            raise Exception()

largest = 999**2
smallest = 100**2

for i in range(largest,smallest,-1):
    if isPalindromic(i): 
        try:
            a,b = integralroots(i)
        except Exception:
            continue
        print "%d x %d = %d"% (a,b,i)
        break

