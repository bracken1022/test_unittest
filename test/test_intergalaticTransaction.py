

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
 #       self.assertTrue(self.intergalaticTransaction.SetCondition("glob glob Silver is 34 Credits"))
        pass
    
    def test_set_conditions_invalid(self):
  #      self.assertFalse(self.intergalaticTransaction.SetCondition("glob inte Glod is 22 Credits"))
        pass

    def test_symbol_value_is_correct(self):
        self.assertEqual("I", self.intergalaticTransaction.symbolValue("glob"))
        self.assertEqual("V", self.intergalaticTransaction.symbolValue("prok"))
        self.assertEqual("X", self.intergalaticTransaction.symbolValue("pish"))
        self.assertEqual("L", self.intergalaticTransaction.symbolValue("tegi"))


def test_suite():
    unittest.TestLoader().LoadTestsFromTestCase(Test_IntergalaticTransaction_Condition_Symbol)
    unittest.TestLoader().LoadTestsFromTestCase(Test_IntergalaticTransaction_Condition_MetalUnit)


if __name__ == "__main__":
    unittest.main()
