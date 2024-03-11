#!/usr/bin/python3
""" Amneity class that inherits BaseModels"""
class Amenity(BaseModel):
    """ Definition oof class"""
    def __init__(self, name = ""):
        self.name = name
