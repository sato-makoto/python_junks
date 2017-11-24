#!/usr/bin/env python3
from sys import argv
original_text = argv[1]
shift = int(argv[2])
l = len(original_text)

ciper_text=''
composite_text=''

for x in range(l):
  ciper_text += chr(ord(original_text[x])+shift)

for x in range(l):
  composite_text += chr(ord(ciper_text[x])-shift)

print("Orig: ",original_text)
print("Cipe: ", ciper_text)
print("Comp: ",composite_text)
