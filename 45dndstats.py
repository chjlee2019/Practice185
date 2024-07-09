"""
In Dungeons and Dragons, each character is described by 6 statistics 
(strength, intelligence, wisdom, dexterity, constitution, charisma). 
In the old days, each stat was decided by summing up the values on 3 six-sided dice (3D6). 
Each stat therefore has a range of 3-18 and an average of 10.5.
Over the years, the official rules have changed and many players have added their own house rules. 
Write a program that determines the average stat value using the various rules below.

3D6: roll 3 six-sided dice
3D6r1: roll 3 six-sided dice, but re-roll any 1s
3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
4D6d1: roll 4 six-sided dice, dropping the lowest die roll

"""
#Roll 3 dice, add them up, a million times.
#Take the average of these million times.
#Practicing loops and conditionals.

#3D6
import random 

rolls = 10
log = rolls // 100 
total = 0
zeroes = 0
for i in range(rolls):
	if i % log == 0: print(f'{100 * i/rolls:.0f}')
	stat = 0
	for sum in range(3, 19):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		d3 = random.randint(1, 6)
		if d1 + d2 + d3 == sum:
			stat += sum
	if stat == 0: zeroes += 1
	total += score
print(total / rolls)
print(zeroes / rolls)

"""
rolls = 10                               # after testing, adapt to 1000's to millions
for i in range (1, rolls + 1):
	print(f'roll no. {i}')
#roll 3 die	 (hint: use a dice rolling simulator)
	for stat in range(3, 19):            # I 
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		d3 = random.randint(1, 6)
#add them up
		if d1 + d2 + d3  == stat:
			print(stat)
#add all of these, then calculate the average. 
   # average = (the sum of scores from all rolls) / (# of rolls)
	return()		

rolls = 10
	for i in range(rolls):
	stat = 0
	for sum in range(3, 19):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		d3 = random.randint(1, 6)
		if d1 + d2 + d3 == sum:
			stat += sum
		print(stat)

"""
#3D6r1
import random 

rolls = 10
log = rolls // 100 
total = 0
zeroes = 0
for i in range(rolls):
	if i % log == 0: print(f'{100 * i/rolls:.0f}')
	# number = 0
	# for number in random.int(1, 6)
		# if number == 1:       [reroll]
	for sum in range(3, 19):
		d1 = random.randint(2, 6)
		d2 = random.randint(2, 6)
		d3 = random.randint(2, 6)
		if d1 + d2 + d3 == sum:
			stat += sum
	if stat == 0: zeroes += 1
	total += score
print(total / rolls)
print(zeroes / rolls)

#3D6x2
rolls = 3
for i in range (1, rolls + 1):
	print(f'roll no. {i}')
	
	for d1 in
	
	# some conditional that prompts to reroll a 1


		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
			d3 = random.randint(1, 6)
			if d1 + d2 + d3  == stat:
				print(stat)


rolls = 3
for i in range (1, rolls + 1):
	print(f'roll no. {i}')
	
# roll two die at a time, take the maximum - then take the maximum
# simulate by hand
		d1a = random.randint(1, 6), d1b* = random.randit(1, 6)
		d2a* = random.randint(1, 6), d2b
		d3a* = random.randint(1, 6), d3b
		if d1b + d2a + d3b == stat:
			print(stat)
# must isolate maximum of each of these three rolls (a or b).


#4D6d1
rolls = 3
for i in range (1, rolls + 1):
	print(f'roll no. {i}')

# how to figure out the lowest, sum up the three? - can't use subsequent
		d1 =
		d2 =
		d3 = 
		d4 = 
# conditionals: which one is lowest? - it's not 
"""