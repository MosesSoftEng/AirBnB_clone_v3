#!/usr/bin/python3
"""Define state routes"""
from api.v1.views import app_views
from models import storage
from flask import jsonify
from flask import request
from models.state import State


@app_views.route(
    '/states',
    methods=['GET', 'POST'],
    strict_slashes=False
)
def get_states():
    """Return list of all states as json"""
    if request.method == 'GET':
        return jsonify(
            [obj.to_dict() for obj in storage.all('State').values()]
        )
    else:
        data = request.get_json();

        state = State(**data)

        print(state)
        return jsonify({})
