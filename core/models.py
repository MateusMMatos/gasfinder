from django.db import models
from django.contrib.auth.models import User

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Localizacao(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    endereco = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.endereco}, {self.cidade}"

class UsuarioProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_cadastro = models.DateField(auto_now_add=True)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

class PostoCombustivel(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)  # Novo campo

    def __str__(self):
        return self.nome

class TipoCombustivel(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class PrecoCombustivel(models.Model):
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    data_atualizacao = models.DateField(auto_now=True)
    posto = models.ForeignKey(PostoCombustivel, on_delete=models.CASCADE)
    tipo_combustivel = models.ForeignKey(TipoCombustivel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.posto} - {self.tipo_combustivel} - {self.valor}"

class Avaliacao(models.Model):
    nota = models.IntegerField()
    comentario = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    posto = models.ForeignKey(PostoCombustivel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.nota}"

class Comentario(models.Model):
    TIPO_COMENTARIO_CHOICES = [
        ('elogio', 'Elogio'),
        ('sugestao', 'Sugestão'),
        ('reclamacao', 'Reclamação'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    posto = models.ForeignKey(PostoCombustivel, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_COMENTARIO_CHOICES)
    texto = models.TextField()
    avaliacao = models.IntegerField(null=True, blank=True)  # Permitir valores nulos
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.posto.nome} - {self.tipo}"

class HistoricoAbastecimento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    posto = models.ForeignKey(PostoCombustivel, on_delete=models.CASCADE)
    preco_combustivel = models.DecimalField(max_digits=5, decimal_places=2)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.posto.nome} - {self.preco_combustivel} - {self.data_hora}"
