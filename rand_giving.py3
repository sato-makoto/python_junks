#!/usr/bin/env python3
# random giving simulation
# https://gigazine.net/news/20170711-random-people-give-money-to-random-other-people/

from random import randint
from random import seed
from sys import argv

times = int(argv[1])
member_list = [100 for x in range(100)]

def give_member():
  return randint(0,99)

def giving():
  for x in range(100):
    member_list[x]-=1
    member_list[give_member()]+=1

for x in range(times):
  seed()
  giving()

print(max(member_list), min(member_list))
