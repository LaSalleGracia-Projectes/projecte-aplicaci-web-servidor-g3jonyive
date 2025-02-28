from flask import Blueprint, jsonify, request
import controllers.company_controller as controller
from utils.utils import make_error_response, need_json
from utils.exceptions import BadRequestException


company = Blueprint(name="company", import_name=__name__, url_prefix="/api/company")

@company.route("/", strict_slashes=False)
def companies():
    response, status = controller.get_all_companies()
    return jsonify(response), status
