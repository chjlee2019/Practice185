"""
Write a program that estimates pi using Monte Carlo methods as was described above. 
Generate random values for x and y from 0 to 1. Calculate the distance to the origin. 
If the distance is less than 1, the point is inside the circle. The ratio of points that fall inside compared to the total is pi/4.
Output each iteration and watch as the ratio gets closer to pi. Use an endless while loop in your program and stop it with ^C.
"""

import math

#Generate random values for x and y from 0 to 1. Calculate the distance to the origin.s
in = 0
out = 0	

while True:
	rx = random.random()
	ry = random.random()
	if dfo(rx, ry) >=1: in += 1
	else:               out += 1
	if in + out % 1000 == 0: print(in, out, in/out)

"""
#If the distance is less than 1, the point is inside the circle (pi/4).

#Output each iteration and watch as the ratio gets closer to pi. Use an endless while loop in your program and stop it with ^C.
#See Unit 3.

while r < pi:
	print ('{r} is getting closer to pi')
	if r == pi: ^C

"""