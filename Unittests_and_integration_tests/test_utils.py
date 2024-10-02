#!/usr/bin/env python3
""" Unittests for utils.py """
import unittest
from unittest.mock import Mock

from requests import patch
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ Unittests for access_nested_map """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])


    def test_access_nested_map_exception(self, nested_map, path):
        """ Test access_nested_map exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(e.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ Unittests for get_json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("https://example.com", {"payload": True}),
    ])
    def test_get_json(self, url, payload):
        """ Test get_json """
        payload = {"payload": True}

        with patch('utils.requests.get') as mock_get:
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = payload
            self.assertEqual(get_json(url), payload)

if __name__ == "__main__":
    unittest.main()