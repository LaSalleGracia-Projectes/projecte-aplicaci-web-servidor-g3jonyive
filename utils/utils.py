from utils.constants import ERROR_RESPONSE
from config import DEBUG
from requests.exceptions import HTTPError
import json

def log(tag: str = "[DEBUG]", message: str = "") -> None:
    if DEBUG:
        print(f"{tag} {message}")
        
def exception_parser(e: HTTPError) -> Exception:
    error_json = e.args[1]
    error_dict = json.loads(error_json).get('error')
    return Exception(f"Error {error_dict.get('code')}: {error_dict.get('message')}")

def make_error_response(error: Exception, status: int) -> dict:
    return {**ERROR_RESPONSE, "details": error}, status