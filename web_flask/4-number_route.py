#!/usr/bin/python3
"""run flask server"""
from flask import Flask, redirect, url_for
app = Flask(__name__)


def makeSpaces(text):
    string = ""
    for i in text:
        if i == '_':
            string += ' '
        else:
            string += i
    return string


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
    return "C {}".format(makeSpaces(text))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyIsFun(text="is cool"):
    """hbnb returned"""
    return "Python {}".format(makeSpaces(text))


@app.route("/number/<int:n>", strict_slashes=False)
def integer(n):
    """hbnb returned"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
