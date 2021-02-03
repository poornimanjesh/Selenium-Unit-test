import unittest
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")

class Test(unittest.TestCase):
    def testAssertisNone(self):
        driver = None
        self.assertIsNone(driver)

    def testAssertisnotNone(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
        self.assertIsNotNone(driver)

if __name__ == "__main__":
    unittest.main()
