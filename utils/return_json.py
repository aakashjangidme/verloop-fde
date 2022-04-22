import json
from flask import jsonify
from exceptions.external_error import ExternalAPIError


def return_json(resp, address):
    """Returns the json output

    Args:
        resp (_type_): response object from geocode api
        address (_type_): address passed in the request

    Returns:
        json: response as requested by the user
    """

    _response = {"address": address, "coordinates": {
        "lat": "", "long": ""}}

    resp = json.loads(resp)

    if resp.get('status', None) == 'OK':
        _response['coordinates'] = resp["results"][0]["geometry"]["location"]
    else:
        raise ExternalAPIError(
            'Something went wrong while requesting coordinates')

    return jsonify(_response)
