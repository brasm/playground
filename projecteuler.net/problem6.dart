#!/usr/bin/env dart
/*
   The sum of the squares of the first ten natural numbers is,
   12 + 22 + ... + 102 = 385

   The square of the sum of the first ten natural numbers is,
   (1 + 2 + ... + 10)2 = 552 = 3025

   Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

   Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
 */
import 'dart:math' as math;

main(){
  int a = 0;
  int b = 0;
  for(int i = 1; i <= 100; i++){
    a += math.pow(i,2);
    b += i;
  }
  print(math.pow(b,2) - a);
}

