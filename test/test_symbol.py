#!/usr/bin/env python

import unittest

from src.symbol import Symbol

class Test_Symbol_AddCondition(unittest.TestCase):
    

    def setUp(self):
        self.symbol = Symbol()

    def tearDown(self):
        pass


    def test_condition_is_valid(self):
        self.assertTrue(self.symbol.AddCondition("glob is I"))

    def test_condition_is_not_str(self):
        self.assertFalse(self.symbol.AddCondition(123))

    def test_condition_is_invalid(self):
        self.assertFalse(self.symbol.AddCondition("glob glob glob"))
        self.assertFalse(self.symbol.AddCondition("globisI"))
        self.assertFalse(self.symbol.AddCondition("I is glob"))
        self.assertFalse(self.symbol.AddCondition("glob is z"))

class Test_Symbol_value(unittest.TestCase):
    

    def setUp(self):
        self.symbol = Symbol()
        self.symbol.AddCondition("glob is I")
        self.symbol.AddCondition("prok is V")
        self.symbol.AddCondition("pish is X")
        self.symbol.AddCondition("tegi is L")

    def tearDown(self):
        pass

    def test_symbol_value_is_correct(self):
        self.assertEqual("I", self.symbol.value("glob"))
        self.assertEqual("V", self.symbol.value("prok"))
        self.assertEqual("X", self.symbol.value("pish"))
        self.assertEqual("L", self.symbol.value("tegi"))

    def test_symbol_value_input_is_invalid(self):
        self.assertEqual("NULL", self.symbol.value("unknown"))

def test_suite():
    unittest.TestLoader().LoadTestsFromTestCase(Test_Symbol_AddCondition)
    unittest.TestLoader().LoadTestsFromTestCase(Test_Symbol_value)



if __name__ == "__main__":
    unittest.main()
