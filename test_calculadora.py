import unittest
from calculadora import suma, resta, multiplicacion, division

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(10, 5), 5)
        self.assertEqual(resta(0, 0), 0)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)
        self.assertEqual(multiplicacion(-2, 4), -8)
        self.assertEqual(multiplicacion(0, 5), 0)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(8, 4), 2)
        self.assertEqual(division(0, 5), 0)
        with self.assertRaises(ValueError):
            division(5, 0)

if __name__ == '__main__':
    unittest.main()
