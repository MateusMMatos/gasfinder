from django.test import TestCase
from .models import PostoCombustivel

class PostoCombustivelTestCase(TestCase):
    def setUp(self):
        PostoCombustivel.objects.create(nome="Posto Teste", localizacao="Teste")

    def test_posto_nome(self):
        posto = PostoCombustivel.objects.get(nome="Posto Teste")
        self.assertEqual(posto.nome, "Posto Teste")