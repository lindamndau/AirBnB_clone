#!/usr/bin/python3
""" Review a class that inherits from BaseModels """
class Review(BaseModels):

    user_id =""
    text = ""
    place_id = ""
    """Definition of Review class"""
    def __init__(self, *args, **kwargs):
        """ __Init__ instance method"""
        super().__init__(*args, **kwargs)
