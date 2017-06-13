from sys import argv

# 12345678 => [12, 34, 56, 78]

arg = int(argv[1])
print(arg)

def fourth_list(num):
  mylist = [0,0,0,0]
  if num < 100:
    mylist[3] = num
  elif num < 100**2:
    mylist[2] = num // 100
    mylist[3] = num % 100
  elif num < 100**3:
    mylist[1] = num // 100**2
    mylist[2] = num % 100**2 // 100
    mylist[3] = num % 100**2 % 100
  else:
    mylist[0] = num // 100**3
    mylist[1] = num % 100**3 // 100**2
    mylist[2] = num % 100**3 % 100**2 // 100
    mylist[3] = num % 100**3 % 100**2 % 100
  return mylist 

if arg < 100**4:
  print(fourth_list(arg))
