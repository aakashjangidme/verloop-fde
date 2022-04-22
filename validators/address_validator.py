from models.address_request import AddressRequest


class AddressValidator(object):
    """Validates the address request body and returns list of error if any

    Args:
        errors ([]): List of error messages that encountered while validating the address request body
    """

    def __init__(self, address_body: AddressRequest) -> None:
        self.address_body = address_body
        self.errors = []

        if not address_body.address:
            self.errors.append('Missing address value')

        valid_formats = {"json", "xml"}
        if address_body.output_format not in valid_formats:
            self.errors.append(
                "Invalid format, Valid values are %s" % (valid_formats))
