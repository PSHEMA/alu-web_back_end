#!/usr/bin/env python3
""" Unittests for client.py """
import unittest
from unittest.mock import patch
from Unittests_and_integration_tests.fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
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
        with patch('client.GithubOrgClient.org',
                   new_callable=property) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
            client = GithubOrgClient("google")
            result = client._public_repos_url
            self.assertEqual(result,
                             "https://api.github.com/orgs/google/repos")

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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test integration """

    @classmethod
    def setUpClass(cls):
        """ Setup class """
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock

        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda y: options.get(y, org_mock)

    @classmethod
    def tearDownClass(cls):
        """ Tear down class """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test public repos """
        org = GithubOrgClient("test")
        repos = org.public_repos()
        payload = self.repos_payload
        self.assertEqual(repos, self.expected_repos)
        self.assertEqual(payload, self.repos_payload)


if __name__ == "__main__":
    unittest.main()
