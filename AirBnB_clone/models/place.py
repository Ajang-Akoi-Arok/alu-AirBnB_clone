#!/usr/bin/python3
"""
This module defines the Place class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that represents a place offered on AirBnB.

    Attributes:
        city_id (str): the id of the City.
        user_id (str): the id of the User (owner).
        name (str): the name of the place.
        description (str): the description of the place.
        number_rooms (int): the number of rooms.
        number_bathrooms (int): the number of bathrooms.
        max_guest (int): the maximum number of guests.
        price_by_night (int): the price per night.
        latitude (float): the latitude.
        longitude (float): the longitude.
        amenity_ids (list): the list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
