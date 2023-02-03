import random

with open('excuses.txt') as f:
	excuses = f.read().splitlines()

key = random.choice(excuses)

print(key)
