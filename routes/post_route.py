from flask import Blueprint, jsonify, request
import controllers.post_controller as controller
from utils.utils import need_json

post = Blueprint(name="post", import_name=__name__, url_prefix="/api/post")

@post.route("/", strict_slashes=False)
def posts():
    response, status = controller.get_all_posts()
    return jsonify(response), status

@post.route("/", strict_slashes=False, methods=["POST"])
@need_json
def add_post():
    # if not request.is_json:
    #     response, status = make_error_response(BadRequestException())
    #     return jsonify(response), status
    
    data = request.get_json()
    
    response, status = controller.add_post(data)
    return jsonify(response), status
