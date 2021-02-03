import unittest
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")

class Test(unittest.TestCase):
    def testAssertlessEqual(self):
        #self.assertLessEqual(10,100)#pass
        self.assertLessEqual(100, 100)#pass
        # self.assertLessEqual(100, 10)#fail


    def testAssertless(self):
        self.assertLess(10,100)#pass
        #self.assertLess(100, 10)  # fail


    def testAssertGrater(self):
        self.assertGreater(100,10)#pass
        #self.assertGreater(10, 100)  #fail

    def testAssertGraterEqual(self):
        self.assertGreaterEqual(100,10)#pass
        #self.assertGreaterEqual(100, 100)  #pass
        #self.assertGreaterEqual(10, 100)  # fail

if __name__ == "__main__":
    unittest.main()











