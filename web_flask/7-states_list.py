#!/usr/bin/python3
"""The `7-states_list` module starts a Flask
application listening on 0.0.0.0 port 5000
"""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(param):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Display a HTML page of a state list"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)
