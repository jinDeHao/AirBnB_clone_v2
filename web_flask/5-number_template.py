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


@app.route("/number_template/<int:n>", strict_slashes=False)
def integer_tmp(n):
    """hbnb returned"""
    return "<!DOCTYPE html>\n<HTML lang=\"en\">\n\t\
<HEAD>\n\t\t\
<TITLE>HBNB</TITLE>\n\t\
</HEAD>\n\t\
<BODY>\n\t\t\
<H1>Number: {}</H1>\n\t\
</BODY>\n</HTML>".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
