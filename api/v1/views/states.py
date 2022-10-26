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
def states():
    """Return a list of states"""
    if request.method == 'GET':
        return jsonify(
            [obj.to_dict() for obj in storage.all('State').values()]
        ), 200
    else:
        data = request.get_json()

        # validate
        if type(data) != dict:
            return jsonify({'error': 'Not a JSON'}), 400

        if data.get('name') is None:
            return jsonify({'error': 'Missing name'}), 400

        state = State(**data)
        state.save()

        return jsonify(state.to_dict()), 201


@app_views.route(
    '/states/<string:state_id>',
    methods=['PUT', 'GET', 'DELETE'],
    strict_slashes=False
)
def state(state_id):
    """Creates, retrieve or deletes a state"""
    state = storage.get(State, state_id)

    if request.method == 'PUT':
        # Get passed body data.
        data = request.get_json()

        # validate
        if type(data) != dict:
            return jsonify({'error': 'Not a JSON'}), 400

        state = State(**data)
        state.save()

        return jsonify(state.to_dict()), 200

    if request.method == 'GET':
        if state is None:
            return jsonify({'error': "Not found"}), 404

        return jsonify(state.to_dict()), 200

    if request.method == 'DELETE':
        if state is None:
            return jsonify({'error': "Not found"}), 404

        state.delete()
        storage.save()
        return jsonify({}), 200
