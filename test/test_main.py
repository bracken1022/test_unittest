#!/usr/bin/env python

import unittest

from src.intergalaticTransaction import IntergalaticTransaction



class Test_MerchantGalaxy(unittest.TestCase):
    

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

    def test_merchantgalaxy(self):
        self.assertEqual(42, self.intergalaticTransaction.CalculateResult("pish tegi glob glob"))
        self.assertEqual(68, self.intergalaticTransaction.CalculateResult("glob prok Silver"))
        self.assertEqual(57800, self.intergalaticTransaction.CalculateResult("glob prok Gold"))
        self.assertEqual(782, self.intergalaticTransaction.CalculateResult("glob prok Iron"))






if __name__ == "__main__":
    unittest.main()
