from rest_framework import viewsets
from .models import (
    Cidade, Localizacao, UsuarioProfile, PostoCombustivel, TipoCombustivel,
    PrecoCombustivel, FotoVerificacao, Avaliacao, Comentario,
    Borracharia, OficinaMecanica, Desconto, CodigoDesconto
)
from .serializers import (
    CidadeSerializer, LocalizacaoSerializer, UsuarioSerializer, PostoCombustivelSerializer,
    TipoCombustivelSerializer, PrecoCombustivelSerializer, FotoVerificacaoSerializer,
    AvaliacaoSerializer, ComentarioSerializer, BorrachariaSerializer, OficinaMecanicaSerializer
)
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = UsuarioProfile.objects.all()
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

def home(request):
    return HttpResponse("Hello, this is the home page!")

def custom_404(request, exception):
    return render(request, 'core/404.html', status=404)

def custom_500(request):
    return render(request, 'core/500.html', status=500)

def home_view(request):
    postos = PostoCombustivel.objects.all()
    context = {
        'postos': postos,
    }
    return render(request, 'home.html', context)

def discounts_view(request):
    descontos = Desconto.objects.all()
    context = {
        'descontos': descontos,
    }
    return render(request, 'discounts.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
