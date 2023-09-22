#!/usr/bin/python3
"""
The `1-hbnb_route` module supplies a function `hello_hbnb`
that starts a Flask web application, listens on 0.0.0.0
port 5000.
Returns:
string 'Hello HBNB!' when queried at '/'
string 'HBNB!' when queried at '/hbnb'
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Returns 'Hello HBNB!' when queried at '/'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns 'HBNB' when queried at '/hbnb'
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
