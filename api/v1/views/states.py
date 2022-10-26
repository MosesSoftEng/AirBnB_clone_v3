#!/usr/bin/python3
"""Define state routes"""
from api.v1.views import app_views
from models import storage
from flask import jsonify


@app_views.route('/states', strict_slashes=False)
def get_states():
    """Return list of all states as json"""
    return jsonify(
        [obj.to_dict() for obj in storage.all('State').values()]
    )
