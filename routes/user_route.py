from flask import Blueprint, jsonify
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