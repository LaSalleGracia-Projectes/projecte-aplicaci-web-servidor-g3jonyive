from utils.exceptions import ValidationError
from validators.validator import Validator

def validate_add_post(data: dict):
    validations = {
        "price": [Validator.is_required, Validator.is_number, Validator.positive_number],
        "user_id": [Validator.is_required, Validator.is_number, Validator.positive_number],
        "title": [Validator.is_required, Validator.is_string],
        "description": [Validator.is_required, Validator.is_string],
        "photo": [Validator.is_string],
        "company_id": [Validator.is_number, Validator.positive_number],
        "specialization_id": [Validator.is_number, Validator.positive_number]
    }
    
    validator = Validator(data, validations)
    validator.validate()
    
    if not validator.status:
        raise ValidationError(validator.errors)
    
def validate_update_post(data: dict):
    validations = {
        "price": [Validator.is_number, Validator.positive_number],
        "title": [Validator.is_string],
        "description": [Validator.is_string],
        "photo": [Validator.is_string],
        "company_id": [Validator.is_number, Validator.positive_number],
        "specialization_id": [Validator.is_number, Validator.positive_number]
    }
    
    validator = Validator(data, validations)
    validator.validate()
    
    if not validator.status:
        raise ValidationError(validator.errors)