#!/usr/bin/python3
"""
a web application with two routes
the web application also entails /python/<text> which replaces underscore with a space
"""
from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello():
    """ prints hello HBNB!"""
    return 'Hello HBNB!'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ prints HBNB"""
    return 'HBNB'
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_',' ')
    return 'C {}'.format(text)
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_route(text = "is cool"):
    text = text.replace('_', ' ')
    return 'python {}'.format(text)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port='5000')
