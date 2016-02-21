

from src.inputValidation import *


import unittest


class Test_InputValidation(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


class Test_IntergalaticTransactionInputValidation(unittest.TestCase):
    

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_input_number(self):
        intergalaticValidation = IntergalaticTransactionInputValidation(123)
        self.assertTrue(intergalaticValidation.IsInValid())


class Test_SymbolInputValidation(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_input_number(self):
        symbolInputValidation = SymbolInputValidation(123)
        self.assertTrue(symbolInputValidation.IsInValid())


    def test_input_glob_is(self):
        symbolInputValidation = SymbolInputValidation("glob is")
        self.assertTrue(symbolInputValidation.IsInValid())

    def test_input_glob_is_I(self):
        symbolInputValidation = SymbolInputValidation("glob is I")
        self.assertFalse(symbolInputValidation.IsInValid())





if __name__ == "__main__":
    unittest.main()
