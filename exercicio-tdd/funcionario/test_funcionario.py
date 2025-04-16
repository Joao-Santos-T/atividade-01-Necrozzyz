"""
Testes da classe Funcionario.
"""
import unittest

from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""
    def setUp(self):
        self.funcionario = Funcionario (
            nome="Arthur Cardoso Telles",
            matricula=2210005,
            salario_hora=50.0,
            horas_trabalhadas=160.0,
            custo_empregador=1200.0,
            tem_comissao=True,
            valor_comissao=200.0,
            contratos_fechados=3
        )

    def test_calcular_salario_bruto(self):
        """Testa o cálculo do salário bruto."""
        esperado = (50.0 * 160.0) + (200.0 * 3)
        resultado = self.funcionario.calcular_salario_bruto()
        self.assertAlmostEqual(resultado, esperado)

    def test_calcular_custo_total(self):
        """Testa o cálculo do custo total."""
        salario_bruto = (50.0 * 160.0) + (200.0 * 3)
        esperado = salario_bruto + 1200.0
        resultado = self.funcionario.calcular_custo_total()
        self.assertAlmostEqual(resultado, esperado)

    def test_calcular_comissao(self):
        """Testa o cálculo da comissão."""
        esperado = 200.0 * 3
        resultado = self.funcionario.calcular_comissao()
        self.assertAlmostEqual(resultado, esperado)

if __name__ == "__main__":
    unittest.main() 