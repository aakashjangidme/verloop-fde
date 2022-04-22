class AddressRequest(object):
    """A model class for address request which is initialzed with dict input from api

    Args:
        address (_type_): The address string to get the co-ordinates for
        output_format (_type_): "json", "xml"
    """
    address: str
    output_format: str

    def __init__(self, d={}):
        self.address = None
        self.output_format = None

        for key in d:
            setattr(self, key, d[key])
