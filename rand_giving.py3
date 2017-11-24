#!/usr/bin/env python3
# random giving simulation
# https://gigazine.net/news/20170711-random-people-give-money-to-random-other-people/

from random import randint
from random import seed
from sys import argv

times = int(argv[1])
rand_max = int(argv[2])
member_list = [100 for x in range(100)]

def give_member():
  return randint(0,99), randint(0,rand_max)

def giving():
  for x in range(100):
    member, amount = give_member()
    if rand_max == 0:
      amount = 1
    member_list[x]-=amount
    member_list[member]+=amount

for x in range(times):
  seed()
  giving()

max_member, min_member = max(member_list), min(member_list)
diff = max_member - min_member
print(max_member, min_member, diff)
