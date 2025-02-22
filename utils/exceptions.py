class ModelNotFoundException(Exception):
    def __init__(self, model_name, field):
        self.model_name = model_name
        self.field = field
        super().__init__(f"{model_name} '{field}' not found.")
        
class ModelAlreadyExistsException(Exception):
    def __init__(self, model_name, field):
        self.model_name = model_name
        self.field = field
        super().__init__(f"{model_name} '{field}' already exists.")