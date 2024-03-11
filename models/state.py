#!/usr/bin/python3
""" state class """
from models.base_model import BaseModel
"""State class that inherits Basemodels attributess"""
class State(BaseModel):
    """ class defined """
    name = ""
    def __init__(self, n*args, **kwargs):
        """ __init__ instance """
        super().__init__(*args, **kwargs)
