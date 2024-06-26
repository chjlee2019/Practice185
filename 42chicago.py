"""
import random
games = 10
for i in range(games + 1):
	print(f'game #{i}')
	for target in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == target:
			print(f'yay, rolled {d1} and {d2} for {target} points')

import random
games = 10
for i in range(1, games + 1):
	print(f'game #{i}')
	for target in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == target:
			print(f'yay, rolled {d1} and {d2} for {target} points')

"""

import random
games = 10
for i in range(1, games + 1):
	print(f'game no. {i}')
	for target in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == target:
			print(f'bueno, you rolled {d1} and {d2} for {target} pts')

games = 1000
for i in range(games):
	score = 0
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
	print(score) # final game score
	
games = 1000000                  # 1 million trials
log = games // 100               # report progress at 1% intervals
total = 0
zeroes = 0
for i in range(games):
	if i % log == 0: print(f'100 * i/games:.0f')
	score = 0
	for target in range(2, 13):	
		if random.randint(1,6) + random.randint(1, 6) == target:
			score += target
	if score == 0: zeroes += 1
	total += score
print(total / games)
print(zeroes / games)