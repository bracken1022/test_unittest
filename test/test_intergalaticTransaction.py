

#!/usr/bin/env python
#encoding=utf-8


import unittest

from src.intergalaticTransaction import IntergalaticTransaction


class Test_IntergalaticTransaction_Condition_Symbol(unittest.TestCase):
    

    def setUp(self):
        self.intergalaticTransaction = IntergalaticTransaction()
        self.intergalaticTransaction.SetCondition("glob is I")
        self.intergalaticTransaction.SetCondition("prok is V")
        self.intergalaticTransaction.SetCondition("pish is X")
        self.intergalaticTransaction.SetCondition("tegi is L")

    def tearDown(self):
        pass

    def test_set_conditions_valid(self):
        self.assertTrue(self.intergalaticTransaction.SetCondition("glob is I"))
        self.assertTrue(self.intergalaticTransaction.SetCondition("prok is V"))

    def test_set_conditions_invalid(self):
        self.assertFalse(self.intergalaticTransaction.SetCondition("""123"""))
        self.assertFalse(self.intergalaticTransaction.SetCondition(123))
        self.assertFalse(self.intergalaticTransaction.SetCondition("""glob is I
g is Z"""))



class Test_IntergalaticTransaction_Condition_MetalUnit(unittest.TestCase):
    

    def setUp(self):
        self.intergalaticTransaction = IntergalaticTransaction()
        self.intergalaticTransaction.SetCondition("glob is I")
        self.intergalaticTransaction.SetCondition("prok is V")
        self.intergalaticTransaction.SetCondition("pish is X")
        self.intergalaticTransaction.SetCondition("tegi is L")
#        self.intergalaticTransaction.SetCondition("glob glob Silver is 34 Credits")


    def tearDown(self):
        pass

    def test_set_conditions_valid(self):
        self.assertTrue(self.intergalaticTransaction.SetCondition("glob glob Silver is 34 Credits"))

    
    def test_set_conditions_invalid(self):
       self.assertFalse(self.intergalaticTransaction.SetCondition("glob inte Glod is 22 Credits"))
 
    def test_symbol_value_is_correct(self):
        self.assertEqual("I", self.intergalaticTransaction.symbolValue("glob"))
        self.assertEqual("V", self.intergalaticTransaction.symbolValue("prok"))
        self.assertEqual("X", self.intergalaticTransaction.symbolValue("pish"))
        self.assertEqual("L", self.intergalaticTransaction.symbolValue("tegi"))

class Test_IntergalaticTransaction_Conversion(unittest.TestCase):
    
    def setUp(self):
        self.intergalaticTransaction = IntergalaticTransaction()
        self.intergalaticTransaction.SetCondition("glob is I")
        self.intergalaticTransaction.SetCondition("prok is V")
        self.intergalaticTransaction.SetCondition("pish is X")
        self.intergalaticTransaction.SetCondition("tegi is L")
        self.intergalaticTransaction.SetCondition("glob glob Silver is 34 Credits")
        self.intergalaticTransaction.SetCondition("glob prok Gold is 57800 Credits")
        self.intergalaticTransaction.SetCondition("pish pish Iron is 3910 Credits")


    def tearDown(self):
        pass

    def test_conversion_symbols(self):
        self.assertEqual(1, self.intergalaticTransaction.CalculateResult("glob"))
        self.assertEqual(5, self.intergalaticTransaction.CalculateResult("prok"))

    def test_conversion_symbols_glob_glob_prok(self):
        self.assertEqual(5, self.intergalaticTransaction.CalculateResult("glob glob prok"))

    def test_conversion_symbols_pish_tegi_glob_glob(self):
        self.assertEqual(42, self.intergalaticTransaction.CalculateResult("pish tegi glob glob"))

    def test_conversion_metal_Silver(self):
        self.assertEqual(17.0, self.intergalaticTransaction.CalculateResult("Silver"))

    def test_conversion_metal_Gold(self):
        self.assertEqual(14450.0, self.intergalaticTransaction.CalculateResult("Gold"))

    def test_conversion_metal_Iron(self):
        self.assertEqual(195.5, self.intergalaticTransaction.CalculateResult("Iron"))

    def test_conversion_symbols_metal_glob_glob_Iron(self):
        self.assertEqual(391, self.intergalaticTransaction.CalculateResult("glob glob Iron"))




def test_suite():
    unittest.TestLoader().LoadTestsFromTestCase(Test_IntergalaticTransaction_Condition_Symbol)
    unittest.TestLoader().LoadTestsFromTestCase(Test_IntergalaticTransaction_Condition_MetalUnit)
    unittest.TestLoader().LoadTestsFromTestCase(Test_IntergalaticTransaction_Conversion)


if __name__ == "__main__":
    unittest.main()
