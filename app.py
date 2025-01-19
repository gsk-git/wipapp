"""
This module creates a Flask application that renders an HTML template.
It defines a root route ('/') that serves the 'index.html' template.
"""
from flask import Flask, render_template

app = Flask(__name__)

# Define root route for this app
@app.route('/')
def home():
    return render_template('index.html')

application = app
