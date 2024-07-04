from rest_framework import viewsets
from .models import (
    Cidade, Localizacao, UsuarioProfile, PostoCombustivel, TipoCombustivel,
    PrecoCombustivel, FotoVerificacao, Avaliacao, Comentario,
    Borracharia, OficinaMecanica, Desconto, CodigoDesconto, HistoricoAbastecimento
)
from .serializers import (
    CidadeSerializer, LocalizacaoSerializer, UsuarioSerializer, PostoCombustivelSerializer,
    TipoCombustivelSerializer, PrecoCombustivelSerializer, FotoVerificacaoSerializer,
    AvaliacaoSerializer, ComentarioSerializer, BorrachariaSerializer, OficinaMecanicaSerializer
)
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import base64
from django.core.files.base import ContentFile
from django.db.models import Avg
from django.views.decorators.http import require_POST
import json
from .forms import CustomUserCreationForm 
from geopy.distance import geodesic 


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
        user_lat = float(request.GET.get('lat', 0))
        user_lng = float(request.GET.get('lng', 0))
        order_by = request.GET.get('order_by', 'preco')  # Padrão é ordenar por preço

        postos = PostoCombustivel.objects.all()

        postos_list = []
        for posto in postos:
            distancia = geodesic((user_lat, user_lng), (posto.localizacao.latitude, posto.localizacao.longitude)).km
            if distancia <= 10:  # Considerar apenas postos dentro de 10 km
                preco_combustivel = PrecoCombustivel.objects.filter(posto=posto).order_by('valor').first()
                preco = preco_combustivel.valor if preco_combustivel else "N/A"
                postos_list.append({
                    'id': posto.id,
                    'nome': posto.nome,
                    'preco': preco,
                    'distancia': round(distancia, 2),
                    'latitude': posto.localizacao.latitude,
                    'longitude': posto.localizacao.longitude,
                    'media_avaliacoes': posto.average_rating if posto.average_rating is not None else 0
                })

        if order_by == 'preco':
            postos_list.sort(key=lambda x: (x['preco'] == "N/A", x['preco']))
        elif order_by == 'distancia':
            postos_list.sort(key=lambda x: x['distancia'])

        return JsonResponse(postos_list, safe=False)
    
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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
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

@login_required
def profile_user_view(request):
    historico = HistoricoAbastecimento.objects.filter(usuario=request.user).order_by('-data_hora')
    context = {
        'historico': historico,
    }
    return render(request, 'core/profileUser.html', context)

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
@require_POST
@csrf_exempt
def submit_rating(request, posto_id):
    posto = get_object_or_404(PostoCombustivel, pk=posto_id)
    data = json.loads(request.body.decode('utf-8'))
    avaliacao = data.get('avaliacao')

    # Tentar buscar a avaliação existente ou criar uma nova
    Avaliacao.objects.update_or_create(
        posto=posto,
        usuario=request.user,
        defaults={'nota': avaliacao}
    )

    # Atualizar a média das avaliações
    media_avaliacoes = Avaliacao.objects.filter(posto=posto).aggregate(Avg('nota'))['nota__avg']
    posto.average_rating = media_avaliacoes
    posto.save()

    return JsonResponse({'status': 'success', 'average_rating': round(media_avaliacoes, 1)})

@login_required
@require_POST
@csrf_exempt
def submit_comment(request, posto_id):
    posto = get_object_or_404(PostoCombustivel, pk=posto_id)
    tipo = request.POST.get('comentario_tipo')
    texto = request.POST.get('comentario')

    comentario = Comentario.objects.create(
        usuario=request.user,
        posto=posto,
        tipo=tipo,
        texto=texto
    )

    return JsonResponse({
        'status': 'success',
        'usuario': comentario.usuario.username,
        'texto': comentario.texto,
        'tipo': comentario.tipo
    })

def posto_profile_view(request, posto_id):
    posto = get_object_or_404(PostoCombustivel, pk=posto_id)
    elogios = Comentario.objects.filter(posto=posto, tipo='elogio')
    sugestoes = Comentario.objects.filter(posto=posto, tipo='sugestao')
    reclamacoes = Comentario.objects.filter(posto=posto, tipo='reclamacao')
    user_rating = Avaliacao.objects.filter(posto=posto, usuario=request.user).first()

    context = {
        'posto': posto,
        'elogios': elogios,
        'sugestoes': sugestoes,
        'reclamacoes': reclamacoes,
        'average_rating': round(posto.average_rating, 1) if posto.average_rating is not None else 0,
        'user_rating': user_rating.nota if user_rating else 0,
    }

    return render(request, 'core/profilePostos.html', context)

def profile_postos_view(request):
    postos = PostoCombustivel.objects.all()
    context = {
        'postos': postos,
    }
    return render(request, 'core/profilePostos.html', context)

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
