#!/usr/bin/python3
"""Define blueprint routes
Routes:
    /status
        Return status ok
    /api/v1/stats
        Return object count stats
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def api_status():
    """Return status ok"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def objects_stats():
    """Return each object type count stats"""
    return jsonify({
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    })
