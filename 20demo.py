# 20demo.py by chjlee2019

import math 

print ('hello world') # greeting

"""
This is a 
multi-line
comment
"""

print (1 + 1)
print (2 ** 3)
print (5 // 3)
print (5 % 3)
print (5 * (3 + 1))

print(math.ceil(2.6))
print(math.floor(2.6))
print (math.log2(3))
print (math.log10(3))
print (math.sqrt(4))
print (0.1 * 1)
print (0.1 * 3)

a = 3							# side of triangle
b = 4							# side of triangle
c = math.sqrt (a**2 + b**2)		# hypotenuse
print(c)

print(type(a), type(b), type(c), sep=', ')

def greeting(): 
	print('hello yourself')
	
def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
	
print(pythagoras(3, 4))
print(pythagoras(1, 1))

# Practice

def arearectangle (a, b):
	return (a * b)
print (arearectangle(2,6))

def temperature (c):
	return (c - 32) * (5/9)
print (temperature(34))

def dsDNAconcentration (d, OD, e):
	return (d * OD * e )
# d = conc., OD = OD260, e = dilution factor
print (dsDNAconcentration(40, 0.65, 50))

def midpoint (x1, y1, x2, y2):
	return ((x1 + x2)/2), ((y1 + y2/2))
print (midpoint(2, 6, 4, 8))