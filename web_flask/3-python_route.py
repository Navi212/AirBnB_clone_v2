#!/usr/bin/python3
"""
The `3-python_route` module supply functions
that starts a Flask web application, listens on 0.0.0.0
port 5000.
Returns:
string 'Hello HBNB!' when queried at '/'
string 'HBNB!' when queried at '/hbnb'
string 'C' followed by the value of text variable replacing
    '_' with space when queried at '/c/<text>'
string 'Python ', followed by the value of the text variable
    '_' with space when queried at '/python/<text>'
"""
from flask import Flask
from markupsafe import escape


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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Returns 'C <value of variable passed>'
    when queried at /c/<text>
    """
    return f"C {text.replace('_', ' ')}"


@app.route('/python/<text>', strict_slashes=False)
def py_text(text="is cool"):
    """
    Returns 'C <value of variable passed>'
    when queried at /python/<text>
    """
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
