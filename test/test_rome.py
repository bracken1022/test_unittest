
import unittest

from src.rome import Rome



class Test_Rome_Input(unittest.TestCase):
    

    def setUp(self):
        self.rome = Rome()
        pass

    def tearDown(self):
        pass


    def test_rome_input_valid(self):
        self.assertTrue(self.rome.IsValid("I"))
        self.assertTrue(self.rome.IsValid("V"))
        self.assertTrue(self.rome.IsValid("X"))
        self.assertTrue(self.rome.IsValid("L"))


    def test_rome_input_invalid(self):
        self.assertFalse(self.rome.IsValid("J"))


class Test_Rome_Calculate(unittest.TestCase):

    def setUp(self):
        self.rome = Rome()

    def tearDown(self):
        pass

    def test_rome_calculate_I(self):
        self.assertEqual(1, self.rome.Calculate("I"))



def suite():
    unittest.TestLoader().LoadTestsFromTestCase(Test_Rome_Input)





if __name__ == "__main__":
    unittest.main()
