import unittest
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")

class Test(unittest.TestCase):
    def testAssertTrue(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
        driver.get("https://www.google.co.uk/")
        print(driver.title)
        titleofwebpage = driver.title
        self.assertTrue("Google" == titleofwebpage)


    def testAssertFalse(self):
         driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
         driver.get("https://www.google.co.uk/")
         print(driver.title)
         titleofwebpage = driver.title
         self.assertFalse("google" == titleofwebpage)


if __name__ == "__main__":
    unittest.main()             
