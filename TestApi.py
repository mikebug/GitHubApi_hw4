
import unittest

from githubhw_4 import get_github_info

class Test(unittest.TestCase):
    def test0_repo(self):
        self.assertEqual(get_github_info(''), "Invalid Inputs")
        self.assertEqual(get_github_info([]), "Invalid Inputs")

if __name__ == '__main__':
    unittest.main()
