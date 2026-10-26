import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_sub(self):
        calc = Calculator()
        result = calc.subtract(10, 6)
        self.assertEqual(result, 4)

        result = calc.subtract(6, 10)
        self.assertEqual(result, -4)

        result = calc.subtract(0, 0)
        self.assertEqual(result, 0)

    def test_mul(self):
        calc = Calculator()
        result = calc.multiply(10, 6)
        self.assertEqual(result, 60)

        result = calc.multiply(6, -10)
        self.assertEqual(result, -60)

        result = calc.multiply(-8, -7)
        self.assertEqual(result, 56)

        result = calc.multiply(0, -0)
        self.assertEqual(result, 0)

    def test_div(self):
        calc = Calculator()
        result = calc.divide(10, 6)
        self.assertAlmostEqual(result, 1.666, 2)

        result = calc.divide(6, -10)
        self.assertAlmostEqual(result, -0.6, 2)

        result = calc.divide(-6, 10)
        self.assertAlmostEqual(result, -0.6, 2)

        result = calc.divide(-6, -10)
        self.assertAlmostEqual(result, 0.6, 2)

        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            calc.divide(0, 0)

        result = calc.divide(0, 8)
        self.assertAlmostEqual(result, 0, 2)

if __name__ == "__main__":
    unittest.main()