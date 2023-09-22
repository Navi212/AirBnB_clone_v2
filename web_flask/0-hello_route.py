#!/usr/bin/python3
"""
The `0-hello_route` supplies a function `hello_hbnb`
that starts a Flask web application, listens to port
5000 on any ip address and returns a string when queried
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Returns 'Hello HBNB!' when queried at '/'
    """
    return f"Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
