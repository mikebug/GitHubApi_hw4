
import unittest

from githubhw_4 import main

class Test(unittest.TestCase):
    def test0_repo(self):
        self.assertEqual(main(''), "Invalid Inputs")
        self.assertEqual(main([]), "Invalid Inputs")

if __name__ == '__main__':
    unittest.main()
