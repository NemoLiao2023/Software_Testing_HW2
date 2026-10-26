import unittest
from Calc_AI import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):

    def test_pow(self):
        calc = Calculator()
        result = calc.pow(2, 3)
        self.assertEqual(result, 8)

if __name__ == "__main__":
    unittest.main()