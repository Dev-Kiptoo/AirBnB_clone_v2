#!/usr/bin/python3
"""
this is a flask script that prints hello world in the 000 500 port
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes = False)

def hello_world():
    """prints hello hbnb!"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = '5000')
