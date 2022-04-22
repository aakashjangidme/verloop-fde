
import xml.etree.ElementTree as ET

from flask import Response

from exceptions.external_error import ExternalAPIError


def return_xml(resp, address):
    """Returns the xml output

    Args:
        resp (_type_): response object from geocode api
        address (_type_): address passed in the request

    Returns:
        xml: response as requested by the user
    """

    _response = ET.fromstring(resp)

    _xml_out = ET.Element("root")

    ET.SubElement(_xml_out, "address").text = address
    coordinates_element = ET.SubElement(_xml_out, "coordinates")
    lat_element = ET.SubElement(coordinates_element, "lat")
    lng_element = ET.SubElement(coordinates_element, "lng")
    lat_element.text = ""
    lng_element.text = ""
    
    if _response.find("status").text == "OK":

        lat_element.text = _response.find("result").find(
            "geometry").find("location").find("lat").text
        lng_element.text = _response.find("result").find(
            "geometry").find("location").find("lng").text
    else:
        raise ExternalAPIError(
            'Something went wrong while requesting coordinates')

    r = Response(response=ET.tostring(_xml_out, encoding="UTF-8", xml_declaration=True), status=200,
                 mimetype="application/xml")

    r.headers["Content-Type"] = "text/xml; charset=utf-8"
    return r
