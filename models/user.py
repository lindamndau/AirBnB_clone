#!/usr/bin/python3
""" Class User that inherits from base class BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Defining Class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ __init__ instaces """
        super().__init__(*args, **kwargs)
