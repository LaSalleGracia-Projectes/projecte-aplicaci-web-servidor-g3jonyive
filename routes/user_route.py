from flask import Blueprint, jsonify, request
import controllers.user_controller as controller


user = Blueprint(name="user", import_name=__name__, url_prefix="/api/user")

@user.route("/")
def users():
    response, status = controller.get_all_users()
    return jsonify(response), status

@user.route("/<string:username>")
def username(username: str):
    response, status = controller.get_user_by_username(username)
    return jsonify(response), status

@user.route("/search/<string:username>")
def search_username(username: str):
    response, status = controller.search_user_by_username(username)
    return jsonify(response), status

@user.route("/add", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Has occurred an error", "details": "The body must be a JSON"}), 400
    
    data = request.get_json()
    
    response, status = controller.add_user(data)
    return jsonify(response), status

@user.route("/delete/<string:uid>", methods=["DELETE"])
def delete_user(uid: str):
    response, status = controller.delete_user(uid)
    return jsonify(response), status