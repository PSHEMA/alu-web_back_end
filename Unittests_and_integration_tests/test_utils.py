#!/usr/bin/env python3
""" Unittests for utils.py """
import unittest
from unittest import mock
from unittest.mock import patch

import requests
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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
        """ Test for get_json method """
        payload = {"payload": True}
        with patch.object(requests, 'get') as mock:
            mock.return_value.json.return_value = payload
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """ Unittests for memoize """

    def test_memoize(self):
        """ Test for memoize method """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()