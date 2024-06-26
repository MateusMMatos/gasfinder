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

class FotoVerificacao(models.Model):
    imagem = models.ImageField(upload_to='verificacoes/', null=True, blank=True)
    data_hora_upload = models.DateTimeField(auto_now_add=True)
    preco = models.ForeignKey(PrecoCombustivel, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    verificado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.preco} - {self.imagem}"
    
class Borracharia(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class OficinaMecanica(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Avaliacao(models.Model):
    nota = models.IntegerField()
    comentario = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    posto = models.ForeignKey(PostoCombustivel, on_delete=models.CASCADE, null=True, blank=True)
    borracharia = models.ForeignKey(Borracharia, on_delete=models.CASCADE, null=True, blank=True)
    oficina_mecanica = models.ForeignKey(OficinaMecanica, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.nota}"

class Comentario(models.Model):
    texto = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    posto = models.ForeignKey(PostoCombustivel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} - {self.posto}"

class Desconto(models.Model):
    posto = models.ForeignKey(PostoCombustivel, on_delete=models.CASCADE)
    percentual = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    imagem_presente = models.ImageField(upload_to='presentes/', null=True, blank=True)
    validade = models.DateField(null=True, blank=True)
    condicoes = models.TextField(null=True, blank=True)
    requer_pontos = models.BooleanField(default=False)
    pontos_necessarios = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.posto} - {self.percentual}%"

class CodigoDesconto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    desconto = models.ForeignKey(Desconto, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10, unique=True)
    usado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario} - {self.desconto} - {self.codigo}"

class PontuacaoUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    pontos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.usuario} - {self.pontos} pontos"
