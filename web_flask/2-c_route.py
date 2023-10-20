#!/usr/bin/python3
"""run flask server"""
from markupsafe import escape
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """hello returned"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb returned"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cIsFun(text):
    """hbnb returned"""
    string = ""
    for i in text:
        if i == '_':
            string += ' '
        else:
            string += i
    return "C {}".format(string)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
