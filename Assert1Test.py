import unittest
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")

class Test(unittest.TestCase):
    def testAssertequalto(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
        driver.get("https://www.google.co.uk/")
        print(driver.title)
        titleofwebpage = driver.title
        self.assertEqual("Google", titleofwebpage, "webpage title are not same")

    def testAssertnotequal(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
        driver.get("https://www.google.co.uk/")
        print(driver.title)
        titleofwebpage = driver.title
        self.assertNotEqual("Googl", titleofwebpage, "webpage title are not same")

if __name__ == "__main__":
     unittest.main()

    






























