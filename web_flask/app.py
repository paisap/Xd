#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template, make_response, jsonify
from routes import home_bp

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(home_bp, url_prefix='/send')


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')