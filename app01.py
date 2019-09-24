import random
from flask import Flask, render_template
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
    idx = random.randint(0, len(results)-1)
    result = results[idx]
    # result = random.choice(results)
    # return f'{result}'
    return render_template('omikuji.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
