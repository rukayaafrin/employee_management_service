#address.py
#defines the address object
from utils.dict_helper import create_dict, dict_to_string
class Address:
    def __init__(self, street, city, postalcode):
        self.street = street
        self.city = city
        self.postalcode = postalcode
        
    def to_dict(self):
        return create_dict(
            street=self.street, 
            city=self.city, 
            postalcode=self.postalcode
        )
