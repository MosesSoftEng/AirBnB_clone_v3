#!/usr/bin/python3
"""Set up flask views blueprint"""
from flask import Blueprint
# Import everything from index.py
from api.v1.views.index import *


# Define a blueprint
app_views = Blueprint(
    'app_views',  # Blueprint name
    __name__,  # Name of blueprint package: for internal routing
    url_prefix='/api/v1'  # Prefix of routes
)
