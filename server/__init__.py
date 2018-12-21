#!/usr/bin/env python3
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from .config import Development

db = SQLAlchemy()
api = Blueprint('api', __name__, url_prefix='/api')

''' Generate application instance based on configuration mode '''
def create_app(mode):
    app = Flask(__name__)
    app.config.from_object(mode)
    # Initialization
    with app.app_context():
        app.register_blueprint(api)
        db.init_app(app)
        db.create_all()
    return app