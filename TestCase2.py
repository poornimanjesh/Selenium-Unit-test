import unittest
from selenium import webdriver
class SerchEnginesTest(unittest.TestCase):
    def test_python(self):
         self.driver=webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
         self.driver.get("https://docs.python.org/3/howto/logging-cookbook.html")
         print("Title page of python :" + self.driver.title)
         self.driver.close()

    def test_amazon(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
        self.driver.get("https://www.amazon.com/")
        print("Title of amazon page :"+ self.driver.title)
        self.driver.close()

if __name__=="__main__":
    unittest.main()






