from flask import Blueprint, jsonify, request
import controllers.specialization_controller as controller
from utils.utils import make_error_response, need_json
from utils.exceptions import BadRequestException


specialization = Blueprint(name="specialization", import_name=__name__, url_prefix="/api/specialization")

@specialization.route("/", strict_slashes=False)
def specializations():
    response, status = controller.get_all_specializations()
    return jsonify(response), status