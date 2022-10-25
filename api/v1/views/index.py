#!/usr/bin/python3
"""Define blueprint routes"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def api_status():
    """Return status ok json"""
    return jsonify({"status": "OK"})
