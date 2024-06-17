# Write a program that finds all Pythagorean triples for triangles with sides a and b less than 100. Specify that range.
# NEVER DO WHAT IT SAYS! SMALLER PROBLEMS FIRST...

import math

"""
limit = 10
for a in range(1, limit):
	for b in range(a + 1, limit):
		c = math.sqrt(a**2 + b**2)
		if c % 1 == 0: print(a,b,c)


limit = 25
for a in range(1, limit):
	for b in range(a + 1, limit):
		c = math.sqrt(a**2 + b**2)
		if c % 1 == 0: print(a,b,c)


limit = 99
for a in range(1, limit):
	for b in range(a + 1, limit):
		c = math.sqrt(a**2 + b**2)
		if c % 1 == 0: print(a,b,c)
"""

limit = 100
for a in range(1, limit):
	for b in range(a + 1, limit):
		c = math.sqrt(a**2 + b**2)
		if c % 1 == 0: print(a,b,c)