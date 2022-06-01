import random

with open('excuses.txt') as f:
	excuses = f.readlines()

key = random.choice(excuses)

print(key)
