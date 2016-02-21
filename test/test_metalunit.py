

import unittest

from src.metalunit import MetalUnit


class Test_MetalUnit(unittest.TestCase):
    

    def setUp(self):
        self.metalUnit = MetalUnit()
        self.metalUnit.AddCondition("Silver", 20)

    def tearDown(self):
        pass

    def test_calculate_Silver(self):
        self.assertEqual(20, self.metalUnit.CalculateResult("Silver"))








if __name__ == "__main__":
    unittest.main()
