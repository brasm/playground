#!/usr/bin/env dart
/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

bool divisible(int number,range){
  if(number < range) return false;
  for(int i = 1; i < range+1; i++){
    if(number.remainder(i) != 0){
      return false;
    }
  }
  return true;
}

main(){
  int i = 0;
  do {
    i+=20;
  } while(! divisible(i,20));
  print(i);
}
