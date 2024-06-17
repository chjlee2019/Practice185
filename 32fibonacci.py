"""
The sequence follows the rule that each number is equal to the sum of the preceding two numbers. 
The Fibonacci sequence begins with the following 14 integers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 ... 
Each number, starting with the third, adheres to the prescribed formula.


A classic programming interview question is to write a program that reports the first 10 numbers from the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34. 
This is a tricky problem. You need to initialize and keep track of 2 previous values.
"""

# must initialize the following: the first number, the second number, the sum of the first and second number, and the sum of consequent consecutive numbers.

limit = 10
n1 = -1								# Initialization is just like bullet points - the hierarchical format of indenting makes sense. 									# Initialization of a first number, n = 0; must be outside the loop; if inside, it will re-initialize every time.
n2 = 1								# Initialization of a second number, n = 1

for n in range(0, limit):
	
	n3 = n1 + n2					# Initialization of a next number needed...but how?
	print(n3)
	
	n1 = n2
	n2 = n3