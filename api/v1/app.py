#!/usr/bin/python3
"""App API version 1 using flask"""
from flask import Flask
from os import getenv
# Create a variable app, instance of Flask.
app = Flask(__name__)

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')

    app.run(host=host, port=port, threaded=True)
