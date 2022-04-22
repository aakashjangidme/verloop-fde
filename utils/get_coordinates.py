import urllib.request
import os
from models.address_request import AddressRequest


def get_coordinates(address_body: AddressRequest):
    """Gets coordinates from google geocode API

    Args:
        address_body (AddressRequest): address request body

    Returns:
        _UrlopenRet: A urllib.Response object to be sent as end-output
    """

    output_format = address_body.output_format
    address = address_body.address

    API_KEY = os.environ.get("GEO_API_KEY")

    url = "https://maps.googleapis.com/maps/api/geocode/%s" % (output_format)

    params = {"address": address, "key": API_KEY}

    query_string = urllib.parse.urlencode(params)

    url = url + "?" + query_string

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        data = response.read()

    return data
