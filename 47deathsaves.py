"""
Death saves are a little different than normal saving throws. 
If your health drops to 0 or below, you are unconscious and may die. 
Each time it is your turn, roll a d20 to determine if you get closer to life or fall deeper into death.
 If the number is less than 10, you record a "failure". If the number is 10 or greater, you record a "success". 
 	elif d < 10: failures += 1
If you are unlucky and roll a 1, it counts as 2 failures. If you're lucky and roll a 20, you gain 1 health and have "revived".
 	elif d == 1: failures += 2 
 If you collect 3 failures, you "die". If you collect 3 successes, you are "stable" but unconscious. 
	else
 If you are unlucky and roll a 1, it counts as 2 failures. If you're lucky and roll a 20, you gain 1 health and have "revived".
 	elif d == 1: failures += 2 
Write a program that simulates death saves. What is the probability one dies, stabilizes, or revives?

"""
import random 

def deathsave():
	successes = 0
	failures = 0
	while True:
		d = random.randint(1, 20)
		if d == 20: return 'revive'
		elif d == 1: failures += 2
		elif d < 10: failures += 1
		else: successes += 1 
	
		if failures >= 3: return 'death'
		if successes >= 3: return 'stable'

trials = 10000
deaths = 0
revives = 0
stables = 0
for i in range(trials):
	result = deathsave()
	if result == 'death': deaths += 1                   # here, the events are not mutually exclusive (sum of probabilities ~100$)
	elif result == 'stable': stables += 1
	else: revives += 1
print(revives / trials)
print(stables / trials)
print(deaths / trials)
	
"""
#break down into simple parts - with a function, without a function?
trials = 10000     # Trial: Did the character die or not? Every trial has three outcomes

failx2 = 0
fail = 0
success = 0
death = 0
stable = 0
revive = 0
d20 = random.randint(1, 20)
	id d20 == 1:  failx2 = failx2 + 1
	if d20 <= 10: fail = fail10 + 1            # or print('fail')
	if d20 >= 10: success = success10 + 1      # or print('success')

# Keep rolling dice to determine how many times you'll need to roll the die to revive.
#
# 10-19: success
# 2-9: failure
#1: abominable failure

# 3 failures: you die
	

# What is probability of death?
print(death / trials)
# What is probability of stabilization?
print(stable / trials)
# what is probability of revival?
print(revive / trials)

# multiple print statements, step-wise
# Stepwise: get one line of code to work, then move on to the next - debug along the way

#e.g. d1 = this, print d1; then confirm with d2; then with d3
"""


