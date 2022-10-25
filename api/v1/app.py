#!/usr/bin/python3
"""App API version 1 using flask"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import jsonify

# Create a variable app, instance of Flask.
app = Flask(__name__)

# Register blueprint app_views
app.register_blueprint(app_views)


# Function to be called when app is popped.
@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close storage"""
    storage.close()


def page_not_found(e):
    return jsonify({'error': "Not found"}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')

    app.register_error_handler(404, page_not_found)

    app.run(host=host, port=port, threaded=True)
