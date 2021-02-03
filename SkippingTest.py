


import unittest


class AppTesting(unittest.TestCase):
    @unittest.SkipTest
    def test_serch(self):
        print("This is searching testing")
    @unittest.skip("This unit is not yet ready")
    def test_prepaid(self):
        print("This is prepaid testing")
    @unittest.skipIf(1==1,"numbers are not equals")
    def test_postpaid(self):
        print("This is postpaid testing")
    def test_payment(self):
        print("This is payment testing")
    def test_gmail(self):
        print("This is gmail testing")
    def test_facebook(self):
        print("This is facebook testing")

if __name__=="__main__":
    unittest.main()