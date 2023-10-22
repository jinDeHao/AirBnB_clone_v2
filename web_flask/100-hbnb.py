#!/usr/bin/python3
"""run flask server"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    """states returned"""
    return render_template('100-hbnb.html\
', states=storage.all("State"), amenities=storage.all('Amenity\
'), places=storage.all("Place"))


@app.teardown_appcontext
def reset(error):
    """reload data"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
