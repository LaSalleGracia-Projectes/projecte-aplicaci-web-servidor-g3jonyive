from flask import Blueprint, jsonify, request
import controllers.like_controller as controller
from utils.utils import make_error_response, need_json
from utils.exceptions import BadRequestException


like = Blueprint(name="like", import_name=__name__, url_prefix="/api/like")

@like.route("/<int:post_id>", strict_slashes=False, methods=["POST"])
def like_post(post_id: int):
    response, status = controller.like_post(post_id)
    return jsonify(response), status