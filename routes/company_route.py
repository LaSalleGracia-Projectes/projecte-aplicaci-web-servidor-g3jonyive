from flask import Blueprint, jsonify, request
import controllers.company_controller as controller
from utils.utils import make_error_response, need_json
from utils.exceptions import BadRequestException


company = Blueprint(name="company", import_name=__name__, url_prefix="/api/company")

@company.route("/", strict_slashes=False)
def companies():
    response, status = controller.get_all_companies()
    return jsonify(response), status

@company.route("/<int:company_id>", strict_slashes=False)
def company_by_id(company_id):
    response, status = controller.get_company_by_id(company_id)
    return jsonify(response), status

@company.route("/<int:company_id>", strict_slashes=False, methods=["DELETE"])
def delete_company(company_id):
    response, status = controller.delete_company(company_id)
    return jsonify(response), status

@company.route("/", strict_slashes=False, methods=["POST"])
def add_company():
    if not request.is_json:
        response, status = make_error_response(BadRequestException())
        return jsonify(response), status
    
    data = request.get_json()
    
    response, status = controller.add_company(data)
    return jsonify(response), status

@company.route("/<int:company_id>", strict_slashes=False, methods=["PATCH", "PUT"])
def update_company(company_id):
    if not request.is_json:
        response, status = make_error_response(BadRequestException())
        return jsonify(response), status
    
    data = request.get_json()
    
    response, status = controller.update_company(company_id, data)
    return jsonify(response), status

