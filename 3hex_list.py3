#from sys import argv
# arg = int(argv[1])

def third_list(num):
  mylist = [0,0,0]
  if num < 256:
    mylist[2] = num
  elif num <256**2:
    mylist[1] = num //256
    mylist[2] = num %256
  else:
    mylist[0] = num //256**2
    mylist[1] = num %256**2 //256
    mylist[2] = num %256**2 %256
  return mylist 

# if arg < 256**3:
# print(arg)
for num in range(256**3-1):
   print(third_list(num))
#else:
#  print("too big!")
