#!/usr/bin/python3
"""script that starts a Flask application"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """display an html page of a list of states"""
    states = storage.all(State)
    return render_template('7-states_list.html')


@app.teardown_appcontext
def close(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    """Main function"""
    app.run(host='0.0.0.0', port=5000)
