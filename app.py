
from flask import Flask, jsonify, request

from exceptions.api_error import APIError
from exceptions.invalid_input import InvalidInput
from models.address_request import AddressRequest
from utils.get_coordinates import get_coordinates
from utils.return_json import return_json
from utils.return_xml import return_xml
from validators.address_validator import AddressValidator
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv('.env')  # load the .env file


@app.errorhandler(APIError)
def handle_exception(err):
    """Return custom JSON when APIError or its children are raised"""
    response = {"error": err.description, "message": ""}
    if len(err.args) > 0:
        response["message"] = err.args[0]
    app.logger.error(f'{err.description}: {response["message"]}')
    return jsonify(response), err.code


# based on the output_format key, the dict will return the function call
resp_dict = {
    'json': lambda x, y: return_json(x, y),
    'xml': lambda x, y: return_xml(x, y)
}


@app.route("/getAddressDetails",  methods=['POST'])
def get_address_api():
    """API function to accept and respond with requested output format for lat & lang for the given address

    Raises:
        InvalidInput: If address request body validation fails

    Returns:
        Response: Response object in the requested format
    """
    body: AddressRequest = AddressRequest(request.json)

    validator: AddressValidator = AddressValidator(body)

    if len(validator.errors):
        raise InvalidInput(validator.errors)

    response = get_coordinates(address_body=body)

    app.logger.info(response)

    output_format = body.output_format

    return resp_dict[output_format](response, body.address)
