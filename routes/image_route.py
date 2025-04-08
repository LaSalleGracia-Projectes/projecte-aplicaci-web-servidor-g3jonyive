from flask import Blueprint, jsonify, request, Response
import controllers.image_controller as controller
from utils.utils import make_error_response
from utils.exceptions import InternalServerError, ModelNotFoundException

image_bp = Blueprint(name="image", import_name=__name__, url_prefix="/api/image")

@image_bp.route("/", strict_slashes=False, methods=["POST"])
def upload_image():
    image = request.files.get('image', None)
    
    try:
        img = controller.save_image(image)
        return jsonify({"image_id": img.id, "url": f"{request.url_root.rstrip('/')}{image_bp.url_prefix}/{img.id}"}), 201
    except ModelNotFoundException:
        response, status = make_error_response(ModelNotFoundException("Image", "image"))
        return jsonify(response), status
    except Exception as e:
        response, status = make_error_response(InternalServerError(str(e)))
        return jsonify(response), status

@image_bp.route("/<int:image_id>", strict_slashes=False, methods=["GET"])
def get_image(image_id: int):
    try:
        image = controller.get_image(image_id)
    except ModelNotFoundException:
        response, status = make_error_response(ModelNotFoundException("Image", image_id))
        return jsonify(response), status
    except Exception as e:
        response, status = make_error_response(InternalServerError(str(e)))
        return jsonify(response), status
    return Response(image.img, mimetype=image.mimetype)