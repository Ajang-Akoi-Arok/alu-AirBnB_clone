#!/usr/bin/python3
"""
This module contains unit tests for the Amenity class.
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_inherits_base_model(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_default_name(self):
        """Test that the default name is an empty string."""
        a = Amenity()
        self.assertEqual(a.name, "")


if __name__ == "__main__":
    unittest.main()
