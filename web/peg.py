from flask import Flask
import random

app = Flask(__name__)

rainbow = "\U0001F308"

@app.route('/')
def get_excuse():
    with open("excuses.txt") as f:
        excuses = f.read().splitlines()
    key = random.choice(excuses)
    return rainbow + "   " + key

if __name__ == '__main__':
    app.run()

