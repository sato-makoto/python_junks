#!/usr/bin/env python3
from sys import argv
shift = int(argv[1])

orig = [chr(x) for x in range(12353,12439)]

words = '親譲りの無鉄砲で小供の時から損ばかりしている。'

for y in words:
  if ord(y) >12352 & ord(y) < 12440:
    if y in orig:
      num = orig.index(y) + shift
      print(orig[num % len(orig)], end='')
    else:
      print(y, end='')

print("")
