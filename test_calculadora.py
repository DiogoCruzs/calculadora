"""
Testes Unitários para a Calculadora
Projeto de Segurança e Auditoria de Sistemas
"""

import unittest
from calculadora import somar, subtrair, multiplicar, dividir


class TestSomar(unittest.TestCase):
    """Testes para a função de soma."""

    def test_soma_positivos(self):
        self.assertEqual(somar(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(somar(-1, -1), -2)

    def test_soma_zero(self):
        self.assertEqual(somar(0, 0), 0)

    def test_soma_decimal(self):
        self.assertAlmostEqual(somar(1.5, 2.3), 3.8)


class TestSubtrair(unittest.TestCase):
    """Testes para a função de subtração."""

    def test_subtracao_positivos(self):
        self.assertEqual(subtrair(10, 3), 7)

    def test_subtracao_resultado_negativo(self):
        self.assertEqual(subtrair(3, 10), -7)

    def test_subtracao_zero(self):
        self.assertEqual(subtrair(5, 0), 5)

    def test_subtracao_decimal(self):
        self.assertAlmostEqual(subtrair(5.5, 2.2), 3.3)


class TestMultiplicar(unittest.TestCase):
    """Testes para a função de multiplicação."""

    def test_multiplicacao_positivos(self):
        self.assertEqual(multiplicar(4, 5), 20)

    def test_multiplicacao_por_zero(self):
        self.assertEqual(multiplicar(100, 0), 0)

    def test_multiplicacao_negativos(self):
        self.assertEqual(multiplicar(-3, -4), 12)

    def test_multiplicacao_decimal(self):
        self.assertAlmostEqual(multiplicar(2.5, 4), 10.0)


class TestDividir(unittest.TestCase):
    """Testes para a função de divisão."""

    def test_divisao_exata(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_divisao_decimal(self):
        self.assertAlmostEqual(dividir(7, 2), 3.5)

    def test_divisao_por_um(self):
        self.assertEqual(dividir(42, 1), 42)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_divisao_negativos(self):
        self.assertEqual(dividir(-10, -2), 5)


class TestSeguranca(unittest.TestCase):
    """Testes de segurança e validação de entrada."""

    def test_tipos_corretos_soma(self):
        """Verifica que soma retorna tipo numérico."""
        resultado = somar(1, 2)
        self.assertIsInstance(resultado, (int, float))

    def test_tipos_corretos_divisao(self):
        """Verifica que divisão retorna tipo numérico."""
        resultado = dividir(10, 3)
        self.assertIsInstance(resultado, (int, float))

    def test_divisao_por_zero_mensagem(self):
        """Verifica que a mensagem de erro é descritiva."""
        with self.assertRaises(ValueError) as contexto:
            dividir(5, 0)
        self.assertIn("zero", str(contexto.exception).lower())


if __name__ == "__main__":
    unittest.main()
