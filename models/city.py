#!/usr/bin/python3
""" City class that inherits BaseModels attributes """
from models.state import State
from models.base_model import BaseModel

class City(BaseModel):
    """ Definition of class """
    def __init__(self, *args, **kwargs):
        name = ""
        state_id = ""
        """ __init__ instance """
        super().__init__(*args, **kwargs)
