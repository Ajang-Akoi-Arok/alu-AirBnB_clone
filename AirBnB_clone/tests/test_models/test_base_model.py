#!/usr/bin/python3
"""
This module contains unit tests for the BaseModel class.
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_id_is_str(self):
        """Test that id is a string."""
        b = BaseModel()
        self.assertIsInstance(b.id, str)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        b = BaseModel()
        self.assertIsInstance(b.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        b = BaseModel()
        self.assertIsInstance(b.updated_at, datetime)

    def test_unique_ids(self):
        """Test that two instances have different ids."""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_str_representation(self):
        """Test the string representation of BaseModel."""
        b = BaseModel()
        s = str(b)
        self.assertIn("[BaseModel]", s)
        self.assertIn(b.id, s)

    def test_save_updates_updated_at(self):
        """Test that save() updates updated_at."""
        b = BaseModel()
        old = b.updated_at
        b.save()
        self.assertGreaterEqual(b.updated_at, old)

    def test_to_dict_has_class_key(self):
        """Test that to_dict includes __class__."""
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")

    def test_to_dict_datetimes_are_strings(self):
        """Test that to_dict converts datetimes to strings."""
        b = BaseModel()
        d = b.to_dict()
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_recreate_from_dict(self):
        """Test recreating an instance from to_dict output."""
        b = BaseModel()
        b.name = "Test"
        b.number = 42
        d = b.to_dict()
        b2 = BaseModel(**d)
        self.assertEqual(b2.id, b.id)
        self.assertEqual(b2.name, "Test")
        self.assertEqual(b2.number, 42)
        self.assertIsInstance(b2.created_at, datetime)


if __name__ == "__main__":
    unittest.main()
