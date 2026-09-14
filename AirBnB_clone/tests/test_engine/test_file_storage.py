#!/usr/bin/python3
"""
This module contains unit tests for the FileStorage class.
"""
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def tearDown(self):
        """Clean up the JSON file after each test."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new() adds an object to storage."""
        b = BaseModel()
        key = "BaseModel.{}".format(b.id)
        self.assertIn(key, storage.all())

    def test_save_creates_file(self):
        """Test that save() creates the JSON file."""
        b = BaseModel()
        b.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_restores_objects(self):
        """Test that reload() restores objects from the JSON file."""
        b = BaseModel()
        b.save()
        storage.reload()
        key = "BaseModel.{}".format(b.id)
        self.assertIn(key, storage.all())

    def test_user_serialization(self):
        """Test serialization and deserialization of User."""
        u = User()
        u.email = "test@test.com"
        u.save()
        storage.reload()
        key = "User.{}".format(u.id)
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key].email, "test@test.com")


if __name__ == "__main__":
    unittest.main()
