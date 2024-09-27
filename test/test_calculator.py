import unittest

from ..src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    # Pruebas unitarias para el cuadrado
    def test_cuadrado_positivo(self):
        calc = Calculator()
        self.assertEqual(calc.cuadrado(5.0), 25.0)

    def test_cuadrado_cero(self):
        calc = Calculator()
        self.assertEqual(calc.cuadrado(0.0), 0.0)

    def test_cuadrado_uno(self):
        calc = Calculator()
        self.assertEqual(calc.cuadrado(1.0), 1.0)

    def test_cuadrado_negativo(self):
        calc = Calculator()
        self.assertEqual(calc.cuadrado(-4.0), 16.0)

    # Pruebas unitarias para el cubo
    def test_cubo_positivo(self):
        calc = Calculator()
        self.assertEqual(calc.cubo(5.0), 125.0)

    def test_cubo_cero(self):
        calc = Calculator()
        self.assertEqual(calc.cubo(0.0), 0.0)

    def test_cubo_uno(self):
        calc = Calculator()
        self.assertEqual(calc.cubo(1.0), 1.0)

    def test_cubo_menos_uno(self):
        calc = Calculator()
        self.assertEqual(calc.cubo(-1.0), -1.0)

    def test_cubo_negativo(self):
        calc = Calculator()
        self.assertEqual(calc.cubo(-4.0), -64.0)

if __name__ == "__main__":
    unittest.main()