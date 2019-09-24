import random

from flask import Flask
import numpy as np

app = Flask(__name__)


@app.route('/hello')
def hello():
    return '<h1>Hello, world</h1>'


@app.route('/goodbye')
def goodbye():
    return 'Goodbye'


@app.route('/add/<a>/<b>')
def add(a, b):
    return str(int(a) + int(b))


@app.route('/omikuji')
def omikuji():
    results = ['大吉', '吉', '凶']
    n = random.randint(0, len(results)-1)
    # result = random.choice(results)
    return f'{results[n]}'


if __name__ == '__main__':
    app.run(debug=True)
