# import first
import random

# initialize
z1 = 0
z2 = 0
z3 = 0
limit = 100000

# define function
for i in range(limit):
	r = random.gauss(0.0, 1.0)
	if r > 1: z1 += 1
	if r > 2: z2 += 1
	if r > 3: z3 += 1

#print output
print (1 - 2*z1/limit)
print (1 - 2*z2/limit)
print (1 - 2*z3/limit)