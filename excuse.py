import random

rainbow = "\U0001F308"

with open("excuses.txt") as f:
    excuses = f.read().splitlines()

key = random.choice(excuses)

print(rainbow + "   " + key)

