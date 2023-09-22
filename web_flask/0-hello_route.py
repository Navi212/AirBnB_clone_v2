#!/usr/bin/python3
"""
The `0-hello_route` module supplies a function
that starts a Flask web application and returns a
text when queried at its root.
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Defines a function that display “Hello HBNB!”
    when queried at its root.
    """
    return f"Hello HBNB!"


if __name__ == "__main__":
    app.run(host=0.0.0.0, port=5000)
