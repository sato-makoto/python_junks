#!/usr/bin/env python3

x = 1/6
while (x <= 0.5 ):
 print('{:4.3f} : {:4.3f}'.format(round(x,3),round((1-x)/5,3)))
 x+=0.01
