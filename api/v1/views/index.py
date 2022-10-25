#!/usr/bin/python3
"""Define blueprint routes"""
from api.v1.views import app_views
import json


@app_views.route('/status', strict_slashes=False)
def api_status():
    """Return status ok json"""
    return json.dumps({"status": "OK"})
