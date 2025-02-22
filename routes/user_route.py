from flask import Blueprint, jsonify, request
import controllers.user_controller as controller
from utils.utils import make_error_response
from utils.exceptions import BadRequestException


user = Blueprint(name="user", import_name=__name__, url_prefix="/api/user")

@user.route("/", strict_slashes=False)
def users():
    response, status = controller.get_all_users()
    return jsonify(response), status

@user.route("/<string:username>", strict_slashes=False,)
def username(username: str):
    response, status = controller.get_user_by_username(username)
    return jsonify(response), status

@user.route("/search/<string:username>", strict_slashes=False)
def search_username(username: str):
    response, status = controller.search_user_by_username(username)
    return jsonify(response), status

@user.route("/", strict_slashes=False, methods=["POST"])
def add_user():
    if not request.is_json:
        response, status = make_error_response(BadRequestException())
        return jsonify(response), status
    
    data = request.get_json()
    
    response, status = controller.add_user(data)
    return jsonify(response), status

@user.route("/<string:username>", strict_slashes=False, methods=["DELETE"])
def delete_user(username: str):
    response, status = controller.delete_user(username)
    return jsonify(response), status

@user.route("/<string:username>", strict_slashes=False, methods=["PUT"])
def update_user(username: str):
    if not request.is_json:
        response, status = make_error_response(BadRequestException())
        return jsonify(response), status
    
    data = request.get_json()
    
    response, status = controller.update_user(username, data)
    return jsonify(response), status