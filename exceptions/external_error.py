from exceptions.api_error import APIError


class ExternalAPIError(APIError):
    """Custom ExternalAPIError Error Class."""
    code = 403
    description = "External API failed"
