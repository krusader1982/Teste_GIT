import unittest
from src.main import soma


class TestSoma(unittest.TestCase):
    def test_retorno_soma_1(self):
        self.assertEqual(soma(10, 10), 20)

    def test_retorno_soma_2(self):
        self.assertEqual(soma(10, 20), 30)

    def test_retorno_soma_3(self):
        self.assertEqual(soma(10, 20), 31)
