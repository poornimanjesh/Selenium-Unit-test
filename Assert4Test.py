import unittest


class Test(unittest.TestCase):
    def testAssertIn(self):
        list = {"python", "java", "net"}
        self.assertIn("pyton", list)  # pass
        # self.assertIn("ruby",list)  #fail

    def testAssertnotIn(self):
        list = {"python", "java", "net"}
        # self.assertNotIn("pyton",list) #fail
        self.assertIn("ruby", list)  # pass

if __name__ == "__main__":
    unittest.main()