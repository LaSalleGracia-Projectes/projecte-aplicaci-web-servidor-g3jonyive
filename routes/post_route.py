from flask import Blueprint, jsonify, request
import controllers.post_controller as controller


post = Blueprint(name="post", import_name=__name__, url_prefix="/api/post")

@post.route("/", strict_slashes=False)
def posts():
    response, status = controller.get_all_posts()
    return jsonify(response), status
