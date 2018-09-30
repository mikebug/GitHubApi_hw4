
import unittest

from githubhw_4 import get_github_info
from unittest import mock

class Test(unittest.TestCase):

    @mock.patch('githubhw_4.get_github_info')
    def test1_repositories(self, mock_get_repositories):
        a = ['Repository Name:GitHubApi_hw4 Number of commits: 15', 'Repository Name:helloworld Number of commits: 3']
        self.assertIn('Repository Name:GitHubApi_hw4 Number of commits: 15', a)
        self.assertIn('Repository Name:helloworld Number of commits: 3', a)



if __name__ == '__main__':
    unittest.main()
