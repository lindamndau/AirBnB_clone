#!/usr/bin/python3
""" user class """
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
""" Place class that inherits attributes and instances form BaseModels"""
class Place(BaseModel):
    """ Definition of class"""
    city_id=""
    user_id=""
    name=""
    description=""
    number_rooms=0
    number_bathrooms=0
    max_guests=0
    price_by_night=0
    latitude=0.0
    longitude=0.0
    amenity_ids=""

    def __init__(self, *args, **kwargs):
    """ __init__ instance="""
        super().__init__(*args, **kwargs)
