import githubhw_4, unittest

class Test(unittest.TestCase):
    def test0_repo(self):
        self.assertEqual(githubhw_4.main(''), "Invalid Inputs")
        self.assertEqual(githubhw_4.main([]), "Invalid Inputs")

if __name__ == '__main__':
    unittest.main()
