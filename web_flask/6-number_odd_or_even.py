#!/usr/bin/python3
"""
The `4-number_route` module supply functions
that starts a Flask web application, listens on 0.0.0.0
port 5000.
Returns:
string 'Hello HBNB!' when queried at '/'
string 'HBNB!' when queried at '/hbnb'
string 'C' followed by the value of text variable replacing
    '_' with space when queried at '/c/<text>'
string 'Python ', followed by the value of the text variable
    '_' with space when queried at '/python/<text>'
display “n is a number” only if n is an integer
display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
"""
from flask import Flask, render_template


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


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    Returns 'C <value of variable passed>'
    when queried at /c/<text>
    """
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text="is cool"):
    """
    Returns 'C <value of variable passed>'
    when queried at /python/<text>
    """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def display_num(n):
    """
    Displays “n is a number” only if n is an integer
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_temp(n):
    """
    Displays a html page only if "n" is an integer
    """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def check_even_odd(n):
    """
    Displays a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
