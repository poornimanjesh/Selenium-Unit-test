import unittest
def setUpModule():
    print("Thin is module testing")

def tearDownModule():
    print("This is teardown module testing")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This is opening aplication login testing")

    @classmethod
    def tearDownClass(cls):
        print("This is application logout testing")

    @classmethod
    def setUp(self):
        print("This is login testing")
        
    @classmethod
    def tearDown(self):
        print("This is logout testing ")


    def test_serch(self):
        print("This is searching testing")
    def test_prepaid(self):
        print("This is prepaid testing")
    def test_postpaid(self):
        print("This is postpaid testing")
    def test_payment(self):
        print("This is payment testing")

if __name__=="__main__":
    unittest.main()