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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """print n is a number if n is a number"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """print an html template"""
    return render_template('templates/5-number.html', n=n)


if __name__ == '__main__':
    """Main function"""
    app.run(host='0.0.0.0', port=5000)
