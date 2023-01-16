#!/usr/bin/python3
"""Using Flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """print a message when route / is used"""
    return "Hello HBNB!"


if __name__ == '__main__':
    """Main function"""
    app.run(host='0.0.0.0', port=5000)
