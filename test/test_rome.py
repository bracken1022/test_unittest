
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
        result = self.rome.Calculate("I")
        self.assertEqual((True, 1), result)

    def test_rome_calculate_V(self):
        self.assertEqual((True, 5), self.rome.Calculate("V"))

    def test_rome_calculate_MMVI(self):
        self.assertEqual((True, 2006), self.rome.Calculate(["M", "M", "V", "I"]))

    def test_rome_calculate_MCMXLIV(self):
        self.assertEqual((True, 1944), self.rome.Calculate(["M", "C", "M", "X", "L", "I", "V"]))

#    def test_rome_calculate_IXL(self):
#        self.assertEqual(59, self.rome.Calculate("IXL"))

    def test_rome_calculate_XXXX(self):
        self.assertFalse(self.rome.Calculate(["M", "M", "X", "X", "X", "X"])[0])

    def test_rome_calculate_III(self):
        self.assertTrue(self.rome.Calculate(["X", "X", "X"])[0])

    def test_rome_calculate_XXMMXX(self):
        self.assertTrue(self.rome.Calculate(["X", "X", "M", "M", "X", "X"])[0])

    def test_rome_calculate_XXIX(self):
        self.assertTrue(self.rome.Calculate(["X", "X", "X", "I", "X"])[0])

#    def test_rome_calculate_XXLX(self):
#        self.assertFalse(self.rome.Calculate(["X", "X", "X", "L", "X"])[0])

    def test_rome_calculate_DDD(self):
        self.assertFalse(self.rome.Calculate(["D", "D", "D"])[0])

    def test_rome_calculate_L(self):
        self.assertEqual((True, 50), self.rome.Calculate("L"))




def suite():
    unittest.TestLoader().LoadTestsFromTestCase(Test_Rome_Input)
    unittest.TestLoader().LoadTestsFromTestCase(Test_Rome_Calculate)





if __name__ == "__main__":
    unittest.main()
