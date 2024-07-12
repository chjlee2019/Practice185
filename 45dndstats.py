"""
3D6: roll 3 six-sided dice
3D6r1: roll 3 six-sided dice, but re-roll any 1s
3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
4D6d1: roll 4 six-sided dice, dropping the lowest die roll
"""

#3D6
# Imagine with props - what's the goal?
# If we have three die, then roll and gather the sum.
import random 

# first, specify a number of rolls. start smalls to debug early.
trials = 10000


# secondly, initialize for sum of those values, which is the stat.
total = 0        # reset after every trials; set up variable on outside.

for i in range(trials):
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	subtotal = d1 + d2 + d3
	total = total + subtotal
average = total / trials       # it only recognizes the last because we didn't save it into a variable that could be remembered.
print(average)

#3D6r1
trials = 10000
total = 0
for i in range(trials):
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	if d1 == 1: d1 = random.randint(1, 6)  
	if d2 == 1:	d2 = random.randint(1, 6)
	if d3 == 1:	d3 = random.randint(1, 6)
	subtotal = d1 + d2 + d3
	total = total + subtotal
average = total / trials
print(average)

#3D6x2
def max2(die):
	d1 = random.randint(1, die)
	d2 = random.randint(1, die)
	if d1 > d2: return d1
	return d2
	
trials = 10000
total = 0
for i in range(trials):
	d1 = max2(6)
	d2 = max2(6)
	d3 = max2(6)
	subtotal = d1 + d2 + d3
	total = total + subtotal
average = total / trials
print(average)
		

#4D6d1: #Create function to find minimum.
def min4(a, b, c, d):
	if a <= b and a <=c and a <=d: return a
	if b<=c and b<=d:              return b
	if c<=d:                       return c
	return d
	
trials = 10000
total = 0
for i in range(trials):
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	subtotal = d1 + d2 + d3 + d4 - min4(d1, d2, d3, d4)
	total = total + subtotal
average = total / trials
print(average)
