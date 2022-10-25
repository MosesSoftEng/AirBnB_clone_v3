#!/usr/bin/python3
"""Set up flask views blueprint"""
from flask import Blueprint


# Define a blueprint
app_views = Blueprint(
    'app_views',  # Blueprint name
    __name__,  # Name of blueprint package: for internal routing
    url_prefix='/api/v1'  # Prefix of routes
)

# Import everything from index.py, import after to avoid circular imports.
from api.v1.views.index import *
