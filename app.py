from flask import Flask, jsonify
from flask_cors import CORS
from config import DATABASE_CONNECTION_URI, DEBUG
from routes.api import api
from utils.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

CORS(app)

app.register_blueprint(api)

@app.before_request
def create_tables():
    import models
    db.create_all()

@app.errorhandler(404)
def page_not_found(error):
    response = {"error": "Page not found"}
    if DEBUG:
        response = {"error": "Page not found", "details": str(error)}
    return jsonify(response), 404


@app.errorhandler(405)
def method_not_allowed(error):
    response = {"error": "Method not allowed"}
    if DEBUG:
        response = {"error": "Method not allowed", "details": str(error)}
    return jsonify(response), 405


@app.errorhandler(Exception)
def handle_exception(error):
    response = {"error": "Internal server error"}
    if DEBUG:
        response = {"error": "Internal server error", "details": str(error)}
    return jsonify(response), 500