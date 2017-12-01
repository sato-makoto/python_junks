#!/usr/bin/env python3
from sys import argv
from fileinput import input
# shift = int(argv[1])
shift = 83

orig = [chr(x) for x in range(12353,12439)]

def shifting(data):
  for y in data:
    if ord(y) >12352 & ord(y) < 12440:
      if y in orig:
        num = orig.index(y) + shift
        print(orig[num % len(orig)], end='')
      else:
        print(y, end='')
print("")

for data in input():
  shifting(data)
