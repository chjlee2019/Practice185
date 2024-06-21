# define a factorial function, and call it.
# n! / k!(n - k)!

"""
Considerations:
k or (n-k) =/=0 (denominator can't equal 0')
n > k: (n-k) > 0 (cannot have negative factorial)

"""

import math

def factorial(n):					#function
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac

def nchoosek(n,k):
	return factorial(n) / (factorial(k) * factorial(n-k))
	

for n in range(1, 11):
	for k in range(1, n):
		print(n, k, nchoosek(n,k))
