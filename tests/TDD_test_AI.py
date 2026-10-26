import unittest
from Calc_AI import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):

    def test_pow(self):
        calc = Calculator()
        result = calc.pow(2, 3)
        self.assertEqual(result, 8)

    def test_pow_zero_to_zero(self):
        calc = Calculator()
        with self.assertRaisesRegex(ValueError, "0 to the power of 0 is undefined"):
            calc.pow(0, 0)

    def test_pow_negative(self):
        calc = Calculator()
        result = calc.pow(2, -2)
        self.assertEqual(result, 0.25)

        with self.assertRaisesRegex(ValueError, "Cannot raise 0 to a negative power"):
            calc.pow(0, -2)



if __name__ == "__main__":
    unittest.main()