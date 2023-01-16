#!/usr/bin/python3
"""Using Flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """print a message when route / is used"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """print a message when /hbnb is used"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """print C plus text"""
    return "C " + text.replace("_", " ")


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """print Python + text"""
    return "Python " + text.replace("_", " ")


if __name__ == '__main__':
    """Main function"""
    app.run(host='0.0.0.0', port=5000)
