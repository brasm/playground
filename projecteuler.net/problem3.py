#!/usr/bin/env python2
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

class factor:
    factors = []

    def __init__(self,number):
        self.factorize(number)
        for n in self.factors:
            print n

    def isPrime(self,number):
        if number == 1: return False
        if number == 2: return True
        if number % 2 == 0: return False
        
        root = math.ceil(math.sqrt(number))
        test = 3
        while (test <= root ):
            if float(number)/float(test) == int(number/test):
                return False
            test+=2
        return True

    def factorize(self,n):
        divided = 0
        while True:
            if n == 1:
                return True
            if self.isPrime(n):
                self.factors.append(n)
                n = 2**divided
                divided = 0
            else:
                n = n/2
                divided += 1


print "Not Correct"
factorme = 600851475143
factor(factorme)
