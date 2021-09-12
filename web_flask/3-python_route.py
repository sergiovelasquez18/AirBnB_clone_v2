#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_holberton():
    """"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text=None):
    """"""
    if text is not None:
        return "Python {}".format(text.replace("_", " "))
    else:
        return "Python is cool"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
