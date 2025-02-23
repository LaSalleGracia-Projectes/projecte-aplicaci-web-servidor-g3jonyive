from utils.constants import ERROR_RESPONSE
from config import DEBUG

def log(tag: str = "[DEBUG]", message: str = "") -> None:
    if DEBUG:
        print(f"{tag} {message}")
        
def make_error_response(exception: Exception) -> dict:
    return {"error": ERROR_RESPONSE, "details": exception.details, "exception": type(exception).__name__}, exception.status_code