"""
One of the classic interview questions is FizzBuzz. 
Make a program that writes out the numbers from 1 to 100. 
If the number is divisible by 3, write Fizz instead. 
If the number is divisible by 5, write Buzz instead. 
If the number is divisible by both 3 and 5, write FizzBuzz.

RULE 1: Don't do what the problem says - always start with a subset of it.
RULE 2: Order of precedence. 
RULE 3: 

"""

#divisible by 3: n % 3 = 0 					(outer loop 1)
#divisible by 5: n % 5 = 0 					(outer loop 2)
# divisible by both 3 and 5: n % 3 and n % 5, or n % (3*5 = 15) 			    (inner loop)

limit = 101							# only this line changes, depending on my input; here, this is a subset.
for n in range(1, limit):			# range is not inclusive, like splice
	if  n % 15	== 0:	print('FizzBuzz')						# order of precedence
	elif n % 5 == 0:    print('Buzz')						# main lesson: order matters!
	elif n % 3 == 0: 	print('Fizz')
	else: 			    print (n)
