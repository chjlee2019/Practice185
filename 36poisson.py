# create a Poisson calculator, look at wiki to check math

# P(x, λ ) =n^k e^-n / k! In Poisson distribution, the mean is represented as E(X) = λ.

"""
(n ** k) * (e ** -n) / math.factorial(k)
"""
import math

def factorial(n):								# name of variable doesn't matter
	if n == 0: return 1
	fac = 1 
	for i  in range(1, n + 1):
		fac = fac * i
	return fac

def poisson(n,k):
	return ((n ** k) * (math.e ** -n)) / math.factorial(k)

for n in range(1, 9):
	for k in range (1, n + 1):
		print (n, k, poisson(n,k))
	



