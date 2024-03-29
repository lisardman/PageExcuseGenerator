from flask import Flask,render_template
from waitress import serve
import random

app = Flask(__name__)

#rainbow = "\U0001F308"

@app.route('/')
def index():
    excuse = get_excuse()
    return render_template("template.html",excuse=excuse)

def get_excuse():
    with open("excuses.txt") as f:
        excuses = f.read().splitlines()
    key = random.choice(excuses)
    return "   " + key

def create_rainbow():
    rainbow = "\U0001F308"
    return rainbow

if __name__ == '__main__':
    #app.run()
    serve(app, host='127.0.0.1', port=5000, threads=4,url_prefix="/lunch")
