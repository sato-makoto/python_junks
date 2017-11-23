#!/usr/bin/env python3
from sys import argv
word = argv[1]
alpha = [chr(x) for x in range(65,91)][::-1]

""" 
暗
号
技
術
の
す
べ
て
P037
"""

for x in range(26):
  lnum = x + 12
  mnum = 14 - x
  if x+12 > 25:
    lnum = x+12 - 26
  if x > 13:
    mnum = 14 - x + 26
  print(lnum,mnum, ": ", end='')
  for y in word:
    ind = alpha.index(y)
    if ind + x > 25:
      print(alpha[ind+x-26].lower(), end='')
    else:
      print(alpha[ind+x].lower(), end='')
  print("")


