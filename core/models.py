from django.db import models

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

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    data_cadastro = models.DateField(auto_now_add=True)
    email = models.EmailField(unique=True)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

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
    caminho_arquivo = models.CharField(max_length=255)
    data_hora_upload = models.DateTimeField(auto_now_add=True)
    preco = models.ForeignKey(PrecoCombustivel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.preco} - {self.caminho_arquivo}"

class Avaliacao(models.Model):
    nota = models.IntegerField()
    comentario = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    posto = models.ForeignKey(PostoCombustivel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} - {self.posto} - {self.nota}"

class Comentario(models.Model):
    texto = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    posto = models.ForeignKey(PostoCombustivel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} - {self.posto}"

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
