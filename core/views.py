from rest_framework import viewsets
from .models import (
    Cidade, Localizacao, Usuario, PostoCombustivel, TipoCombustivel,
    PrecoCombustivel, FotoVerificacao, Avaliacao, Comentario,
    Borracharia, OficinaMecanica
)
from .serializers import (
    CidadeSerializer, LocalizacaoSerializer, UsuarioSerializer, PostoCombustivelSerializer,
    TipoCombustivelSerializer, PrecoCombustivelSerializer, FotoVerificacaoSerializer,
    AvaliacaoSerializer, ComentarioSerializer, BorrachariaSerializer, OficinaMecanicaSerializer
)
from django.shortcuts import render

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PostoCombustivelViewSet(viewsets.ModelViewSet):
    queryset = PostoCombustivel.objects.all()
    serializer_class = PostoCombustivelSerializer

class TipoCombustivelViewSet(viewsets.ModelViewSet):
    queryset = TipoCombustivel.objects.all()
    serializer_class = TipoCombustivelSerializer

class PrecoCombustivelViewSet(viewsets.ModelViewSet):
    queryset = PrecoCombustivel.objects.all()
    serializer_class = PrecoCombustivelSerializer

class FotoVerificacaoViewSet(viewsets.ModelViewSet):
    queryset = FotoVerificacao.objects.all()
    serializer_class = FotoVerificacaoSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class BorrachariaViewSet(viewsets.ModelViewSet):
    queryset = Borracharia.objects.all()
    serializer_class = BorrachariaSerializer

class OficinaMecanicaViewSet(viewsets.ModelViewSet):
    queryset = OficinaMecanica.objects.all()
    serializer_class = OficinaMecanicaSerializer

def custom_404(request, exception):
    return render(request, 'core/404.html', status=404)

def custom_500(request):
    return render(request, 'core/500.html', status=500)
