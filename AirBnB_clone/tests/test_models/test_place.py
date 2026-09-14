#!/usr/bin/python3
"""
This module contains unit tests for the Place class.
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_inherits_base_model(self):
        """Test that Place inherits from BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_defaults(self):
        """Test the default attributes of Place."""
        p = Place()
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
