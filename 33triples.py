"""
Write a program that finds all Pythagorean triples for triangles with sides a and b less than 100. 
For example, 3, 4, 5 is a triple: 3^2 + 4^2 = 5^2. Hint: all sides, including the hypotenuse, must be an integer. 
A good way to test for an integer is if c % 1 == 0. 
There are 62 unique triples (half-matrix minus the major diagonal).

Pythagorean triples are a2+b2 = c2 where a, b and c are the three positive integers. 
These triples are represented as (a,b,c). 
Here, a is the perpendicular, b is the base and c is the hypotenuse of the right-angled triangle. 
The most known and smallest triplets are (3,4,5).

(3, 4, 5)
(5, 12, 13)
(7, 24,25)
(8, 15, 17)
(9, 40, 41)
(11, 60, 61)
(12, 35, 37)
(13, 84, 85)
"""

# Write a program that finds all Pythagorean triples for triangles with sides a and b less than 100. Specify that range.
# NEVER DO WHAT IT SAYS! SMALLER PROBLEMS FIRST...

import math

limit = 100
for a in range(1, limit):
	for b in range(a + 1, limit):
		c = math.sqrt(a**2 + b**2)
		if c % 1 == 0: print(a,b,c)


	#"There are 62 unique triples (half-matrix minus the major diagonal), which means an inner loop must start at (a+1)."
	# a must start at 1, and the initialization of variable a must specify that.
	# but b and c are ""
	
"""		

# Second condition: if above is satisfied, print the values of a, b, and c only if the sum of a2 + b2 = c2.
	if a**2 + b**2 == c**2:		print(a, b, c)	
	else:						print('false')		# necessary? unless I can simply have nothing print instead.



===============

a2 + b2 = c2

1 + 1 = 2 = 1.41
1 + 2 = sqr(3)			# half matrix (we don't need to do both 1 + 2 AND 2 + 1 - no need to do in diagonal.)
2 + 1 = sq
3 + 5 = sqr 8 
9 + 16 = 25 

"""

