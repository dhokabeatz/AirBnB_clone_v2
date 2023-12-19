#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestConsoleCreate(unittest.TestCase):
    """Test the create command in the console."""

    def setUp(self):
        """Set up the mock stdin and stdout."""
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()
        self.mock_stdin = StringIO()

    def tearDown(self):
        """Clean up after each test."""
        self.mock_stdout.close()
        self.mock_stdin.close()

    def test_create_with_params(self):
        """Test create command with parameters."""
        with patch('sys.stdout', self.mock_stdout), patch('sys.stdin', self.mock_stdin):
            self.console.onecmd("create BaseModel name=\"test\" number=42")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output, 'BaseModel name="test" number=42')

            # Check if the created instance is stored in __objects
            key = "BaseModel." + output
            self.assertIn(key, storage.all())

    def test_create_invalid_class(self):
        """Test create command with an invalid class."""
        with patch('sys.stdout', self.mock_stdout), patch('sys.stdin', self.mock_stdin):
            self.console.onecmd("create InvalidClass name=\"test\" number=42")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_create_missing_class(self):
        """Test create command with missing class."""
        with patch('sys.stdout', self.mock_stdout), patch('sys.stdin', self.mock_stdin):
            self.console.onecmd("create")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_invalid_params(self):
        """Test create command with invalid parameters."""
        with patch('sys.stdout', self.mock_stdout), patch('sys.stdin', self.mock_stdin):
            self.console.onecmd("create BaseModel invalid_param=\"test\"")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "BaseModel invalid_param=\"test\": invalid attribute")

    def test_create_quoted_value(self):
        """Test create command with a quoted value."""
        with patch('sys.stdout', self.mock_stdout), patch('sys.stdin', self.mock_stdin):
            self.console.onecmd("create BaseModel name=\"My_little_house\"")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output, 'BaseModel name="My little house"')

            # Check if the created instance is stored in __objects
            key = "BaseModel." + output
            self.assertIn(key, storage.all())


if __name__ == '__main__':
    unittest.main()
