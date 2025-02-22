from datetime import datetime

class Validator:
    def __init__(self, data: dict, validations: dict):
        self.status = True
        self.errors = []
        self.data = data
        self.validations = validations
        
    def validate(self):
        for key, value in self.validations.items():
            for validation in value:
                field = self.data.get(key, None)
                if isinstance(validation, list):
                    status, message = validation[0](self, field, validation[1])
                else:
                    status, message = validation(self, field)
                if not status:
                    self.add_error(key, message)
                    break
    
    def is_required(self, value):
        if value is None:
            return False, 'The field is required'
        return True, ''
    
    def is_number(self, value):
        if not value.isnumeric():
            return False, 'The field must be a number'
        return True, ''
    
    def positive_number(self, value):
        if int(value) < 0:
            return False, 'The field must be a positive number'
        return True, ''
    
    def is_string(self, value):
        if not isinstance(value, str):
            return False, 'The field must be a string'
        return True, ''
    
    def is_date(self, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            return False, 'The field must be a date, format: YYYY-MM-DD'
        return True, ''
    
    def is_email(self, value):
        if not '@' in value or not '.' in value:
            return False, 'The field must be an email'
        return True, ''
    
    def is_boolean(self, value):
        if not isinstance(value, bool) and not value in ["True", "False"] and not value in [1, 0]:
            return False, 'The field must be a boolean value'
        value = value == "True" or value == 1
        return True, ''
    
    def equals(self, value, values):
        if value not in values:
            return False, f'The field must be one of the following values: {values}'
        return True, ''
    
    def add_error(self, key: str, message: str):
        self.errors.append({key: message})
        self.status = False