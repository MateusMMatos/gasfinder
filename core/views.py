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
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse
from .models import PostoCombustivel, Desconto, FotoVerificacao, HistoricoAbastecimento
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import base64
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

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

class PostosListView(View):
    def get(self, request, *args, **kwargs):
        postos = PostoCombustivel.objects.all().values('nome', 'localizacao__latitude', 'localizacao__longitude')
        return JsonResponse(list(postos), safe=False)

class DescontosListView(View):
    def get(self, request, *args, **kwargs):
        descontos = Desconto.objects.all().values('posto__nome', 'percentual', 'descricao')
        return JsonResponse(list(descontos), safe=False)

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

def emergency_view(request):
    return render(request, 'emergency.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def locator_view(request):
    return render(request, 'core/locator.html')

def neighborhood_discovery_view(request):
    return render(request, 'core/neighborhoodDiscovery.html')

def mapa_simples_view(request):
    return render(request, 'core/mapaSimples.html')

def travel_times_view(request):
    return render(request, 'core/travelTimes.html')

def address_selection_view(request):
    return render(request, 'core/addressSelection.html')

def profile_user_view(request):
    return render(request, 'core/profileUser.html')

@csrf_exempt
def capture_image(request):
    if request.method == 'POST':
        imagem_data = request.POST.get('imagem')
        format, imgstr = imagem_data.split(';base64,') 
        ext = format.split('/')[-1] 
        data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        FotoVerificacao.objects.create(imagem=data)
        return redirect('home')
    return render(request, 'capture_image.html')

@login_required
def profile_user_view(request):
    historico = HistoricoAbastecimento.objects.filter(usuario=request.user).order_by('-data_hora')
    context = {
        'historico': historico,
    }
    return render(request, 'core/profileUser.html', context)

def posto_profile_view(request, posto_id):
    posto = get_object_or_404(PostoCombustivel, pk=posto_id)
    elogios = Comentario.objects.filter(posto=posto, tipo='elogio')
    sugestoes = Comentario.objects.filter(posto=posto, tipo='sugestao')
    reclamacoes = Comentario.objects.filter(posto=posto, tipo='reclamacao')
    context = {
        'posto': posto,
        'elogios': elogios,
        'sugestoes': sugestoes,
        'reclamacoes': reclamacoes,
    }
    return render(request, 'core/posto_profile.html', context)

@login_required
def submit_comment(request, posto_id):
    if request.method == 'POST':
        posto = get_object_or_404(PostoCombustivel, pk=posto_id)
        tipo = request.POST.get('comentario_tipo')
        texto = request.POST.get('comentario')
        avaliacao = request.POST.get('avaliacao')
        Comentario.objects.create(
            usuario=request.user,
            posto=posto,
            tipo=tipo,
            texto=texto,
            avaliacao=avaliacao
        )
        return redirect('posto_profile', posto_id=posto_id)

