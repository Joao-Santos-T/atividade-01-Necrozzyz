import unittest
from datetime import datetime, timedelta
from produto import Produto

class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.produto = Produto(
            codigo="001",
            nome="Caneta",
            preco=2.50,
            quantidade=20,
            data_validade=datetime.now() + timedelta(days=30), 
            estoque_minimo=10
        )

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        self.assertEqual(self.produto.codigo, "001")
        self.assertEqual(self.produto.nome, "Caneta")
        self.assertEqual(self.produto.preco, 2.50)
        self.assertEqual(self.produto.quantidade, 20)
        self.assertGreater(self.produto.data_validade, datetime.now())
        self.assertEqual(self.produto.estoque_minimo, 10)

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        self.produto.adicionar_estoque(10)
        self.assertEqual(self.produto.quantidade, 30)

    def test_adicionar_estoque_negativo(self):
        """Verifica se adicionar uma quantidade negativa lança um erro."""
        with self.assertRaises(ValueError):
            self.produto.adicionar_estoque(-5)

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        resultado = self.produto.remover_estoque(5)
        self.assertTrue(resultado)
        self.assertEqual(self.produto.quantidade, 15)

        resultado = self.produto.remover_estoque(50) 
        self.assertFalse(resultado)

    def test_remover_estoque_zero(self):
        """Verifica se tentar remover 0 itens do estoque lança um erro."""
        with self.assertRaises(ValueError):
            self.produto.remover_estoque(0)

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        self.assertFalse(self.produto.verificar_estoque_baixo())
        self.produto.remover_estoque(15)
        self.assertTrue(self.produto.verificar_estoque_baixo())

    def test_calcular_valor_total(self):
        """Verifica se o valor total é calculado corretamente."""
        esperado = 2.50 * 20
        self.assertEqual(self.produto.calcular_valor_total(), esperado)

    def test_verificar_validade(self):
        """Verifica se a validação de data de validade funciona corretamente."""
        self.assertTrue(self.produto.verificar_validade())

        produto_vencido = Produto(
            codigo="002",
            nome="Borracha",
            preco=1.00,
            quantidade=10,
            data_validade=datetime.now() - timedelta(days=1)
        )
        self.assertFalse(produto_vencido.verificar_validade())

    def test_verificar_validade_none(self):
        """Verifica se a validade é considerada válida quando a data de validade é None."""
        produto_sem_validade = Produto(
            codigo="003",
            nome="Produto Sem Validade",
            preco=5.00,
            quantidade=10,
            data_validade=None 
        )
        self.assertTrue(produto_sem_validade.verificar_validade())

if __name__ == "__main__":
    unittest.main()
