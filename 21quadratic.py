# Solve quadratic equation.
# Two separate functions since I could not find a plus and minus operator.

import math

def quadratic (a, b, c):
	return (-b + (b**2 + math.sqrt(4*a*c)))/(2*a)
	
print(quadratic(2, 3, 6))		#x1
print (quadratic(4, 6, 7))		#x2
print (quadratic (5, 7, 9))		#x3

def quadratic (a, b, c):
	return (-b + (b**2 - math.sqrt(4*a*c)))/(2*a)

print(quadratic(2, 3, 6))		#x1
print (quadratic(4, 6, 7))		#x2
print (quadratic (5, 7, 9))		#x3