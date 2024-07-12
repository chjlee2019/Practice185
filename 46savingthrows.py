

# One of the core mechanics of D&D is the "saving throw". 
# When certain events happen, you need to roll a d20 to figure out if you succeed or not. 
# For example, you are walking across a frozen lake and it begins to crack underfoot. 
# If you make a saving throw, you step aside. If you fail, you fall in.
 
#1D20?
import random 

trials = 10000
# Some saving throws are more difficult than others. 
# If the ice is very thick, the "difficulty class" (DC) may be only 5. 
# This means you only need to roll a 5 or higher to succeed. 
for dc in range(5, 16, 5):     #every dc has its own 10,000 roll x 3 = 30,000
	normal = 0 
	for i in range(trials):
		d20 = random.randint(1, 20) #is the number greater than the difficulty class?
		if d20 >= dc: normal = normal + 1
	print(dc, normal / trials)

""""	
saves5 = 0
saves10 = 0
saves15 = 0     # whereas this one rolls once per condition
for i in range(trials):
	d20 = random.randint(1, 20)
	if d20 >= 5: saves5 = saves5 + 1
	if d20 >= 10: saves10 = saves10 + 1
	if d20 >= 15: saves15 = saves15 + 1
print(saves5 / trials)
print(saves10 / trials)
print(saves15 / trials)

# Same number of conditional statements, but not for the number of random integers generated.
# The second saves a lot of time. For more expensive operations, this can be favorable.
# The first is simpler/more abstract/more elegant/faster to write...sometimes*; the second is more repetition/faster to run.
# *Abstraction can take a lot of time to write at first...
# Is it the right, or the least wrong? That can depend on our understanding
  # Dr. Korf's tip: have both, and choose.
# The faster one usually has bugs in it - it can tend to involve more typing, and hence be more complicated.
 # the slower one is good for debugging; it's well-validated and perfect
 # the slower's like a calibration tool

# ~80% 20 - 5 + 1
# However, if the ice is thin and has a DC of 15, you will need a roll of 15 or higher to succeed.

"""

# Certain events may give you "advantage" or "disadvantage". For example, if you have a rope tied around your waist and a friend is instructed to pull you aside if anything bad happens, you could have "advantage". 
# This allows you to roll two d20s and take the larger value. You may also have disadvantage, for example another "friend" pushes you from behind, causing you to stumble forward. 
# In this case, you have "disadvantage" and must take the lower of two d20 rolls.
# where do each of the initializations go in each loop?
 
# What is the probability of success normally or with advantage/disadvantage? 
print('--')
for dc in range(5, 16, 5):
	normal = 0                   #initializing 0's
	adv = 0
	dis = 0
	for i in range(trials):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)		
		if d1 >= dc:                normal += 1
		if d1 >= dc or d2 >= dc:    adv += 1
		if d1 >= dc and d2 >= dc:   dis += 1
	print(dc, normal / trials)   # report for dc5, dc10, and dc15
	print(dc, adv / trials)      # total, 9
	print(dc, dis / trials)
	
# The big takeaway: Must have three initializations that reset and report the variables each time through the loop.
# Initializations can be easy to misplace.

