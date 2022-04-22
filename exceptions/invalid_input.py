
from exceptions.api_error import APIError


class InvalidInput(APIError):
    """Custom InvalidInput Error Class."""
    code = 403
    description = "Invalid Input Parameter Error"
