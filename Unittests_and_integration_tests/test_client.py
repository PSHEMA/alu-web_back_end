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
    @patch('client.get_json', return_value={
        "repos_url": "https://api.github.com/orgs/google/repos"
    })
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
        })

    def test_public_repos_url(self):
        """Test the _public_repos_url property"""
        with patch('client.GithubOrgClient.org', new_callable=property) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
            client = GithubOrgClient("google")
            result = client._public_repos_url
            self.assertEqual(result, "https://api.github.com/orgs/google/repos")

    @patch("client.get_json")
    def test_public_repos(self, mock):
        """Test public repos"""
        mock.return_value = [{"name": "testing"}, {"name": "todo-app"}]
        with patch.object(
            GithubOrgClient, '_public_repos_url',
            return_value="https://api.github.com/orgs/izzy"
        ):
            org = GithubOrgClient("izzy")
            self.assertEqual(org.public_repos(), ["testing", "todo-app"])
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
