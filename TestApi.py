
import unittest

from githubhw_4 import main
class Test(unittest.TestCas):
    def test0_repo(self):
        self.assertEqual(githubhw_4.main(''), "Invalid Inputs")
        self.assertEqual(githubhw_4.main([]), "Invalid Inputs")

if __name__ == '__main__':
    unittest.main()
