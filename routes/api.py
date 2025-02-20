from flask import Blueprint, jsonify


api = Blueprint(name="api", import_name=__name__, url_prefix="/api")

@api.route("/")
def hello_world():
    return jsonify({"message": "Hello, World!"})