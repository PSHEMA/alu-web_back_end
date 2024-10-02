#!/usr/bin/env python3
""" Unittests for client.py """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json

class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"repos_url": "https://api.github.com/orgs/google/repos"})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {"repos_url": f"https://api.github.com/orgs/{org_name}/repos"})
    
    @patch('client.get_json', return_value={"repos_url": "https://api.github.com/orgs/google/repos"})
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the correct value"""
        client = GithubOrgClient("google")
        result = client.public_repos
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/google/repos")
        self.assertEqual(result, {"repos_url": "https://api.github.com/orgs/google/repos"})


if __name__ == "__main__":
    unittest.main()
