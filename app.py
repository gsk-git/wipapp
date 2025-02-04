"""
This module creates a Flask application that renders an HTML template.
It defines a root route ('/') that serves the 'index.html' template.
"""
import os
from flask import Flask, render_template
from dotenv import load_dotenv, dotenv_values

app = Flask(__name__)
load_dotenv()
env=os.getenv("MAPS_API")

# Define root route for this app
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/maps')
def maps():
    return render_template('maps.html', env=env)

application = app
