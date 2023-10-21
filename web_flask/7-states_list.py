#!/usr/bin/python3
"""run flask server"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


def sortdict(dictionary):
    diction = {}
    for i in dictionary:
        diction[i] = dictionary[i]


@app.route("/states_list", strict_slashes=False)
def states():
    """states returned"""
    return render_template('7-states_list.html', states=storage.all("State"))


@app.teardown_appcontext
def reset(error):
    """reload data"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
