"""
Estimate pi using the Nilakantha series. 
Hint: you must figure out how to get the +/- to flip-flop with each iteration.

Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) ...

# 2, 4 , 6, 8 = by multiples of 

"""
import math

# First, create a function for the iteration, 4 / (n * (n+1) * (n+2))
def iteration(n):
	if n == 0: return 1
	if n == 1: return 1
	it = 2
	for i in range(2, n + 2, 2):
		it = (4 / (i * (i + 1) * (i + 2)) - (4 / (i + 2) * (i + 3) * (i + 4))
	return it	


# Next, define the Nilikantha series.
def nilakantha(n):
	return: 3 + iteration(n) + iteration(n + 4)
	#stuck on the flip-flop here
	
	
	
for n in range (2, n + 2, 2):	
	print nilikantha(n)
	
	n = 1
	
