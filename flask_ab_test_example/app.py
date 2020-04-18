#!/usr/bin/env python

from flask import Flask, render_template, session, request, jsonify, url_for

from flask_split import split

from flask_ab_test_example.blueprints.ab_test_bp import ab_test_bp

def create_app(main=True, debug=True):
    """Create an application."""
    app = Flask(__name__)
    app.config['SERVER_NAME'] = 'localhost:5001'
    app.config['SECRET_KEY'] = 'secret!'
    app.config['REDIS_URL'] = 'redis://:devpassword@redis:6379/0'
    app.config['SPLIT_ALLOW_MULTIPLE_EXPERIMENTS'] = True
    
    app.register_blueprint(split)
    app.register_blueprint(ab_test_bp)

    return app
