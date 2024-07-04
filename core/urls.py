from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CidadeViewSet, LocalizacaoViewSet, UsuarioViewSet, PostoCombustivelViewSet, TipoCombustivelViewSet,
    PrecoCombustivelViewSet, FotoVerificacaoViewSet, AvaliacaoViewSet, ComentarioViewSet,
    BorrachariaViewSet, OficinaMecanicaViewSet, home_view, discounts_view, register_view,
    login_view, logout_view, PostosListView, DescontosListView, capture_image, emergency_view,locator_view, neighborhood_discovery_view, 
    mapa_simples_view, travel_times_view, address_selection_view, profile_user_view, posto_profile_view, submit_comment, profile_postos_view
)

router = DefaultRouter()
router.register(r'cidades', CidadeViewSet)
router.register(r'localizacoes', LocalizacaoViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'postos', PostoCombustivelViewSet)
router.register(r'tipos_combustivel', TipoCombustivelViewSet)
router.register(r'precos_combustivel', PrecoCombustivelViewSet)
router.register(r'foto_verificacao', FotoVerificacaoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'borracharias', BorrachariaViewSet)
router.register(r'oficinas_mecanicas', OficinaMecanicaViewSet)

urlpatterns = [
    path('', home_view, name='home'),
    path('descontos/', discounts_view, name='descontos'),
    path('registrar/', register_view, name='registrar'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/postos/', PostosListView.as_view(), name='api_postos'),
    path('api/descontos/', DescontosListView.as_view(), name='api_descontos'),
    path('api/', include(router.urls)),
    path('capture/', capture_image, name='capture_image'),
    path('emergency/', emergency_view, name='emergency'),
     path('locator/', locator_view, name='locator'),
    path('neighborhood-discovery/', neighborhood_discovery_view, name='neighborhood_discovery'),
    path('mapa-simples/', mapa_simples_view, name='mapa_simples'),
    path('travel-times/', travel_times_view, name='travel_times'),
    path('address-selection/', address_selection_view, name='address_selection'),
    path('profile-user/', profile_user_view, name='profile_user'),
    path('posto/<int:posto_id>/', posto_profile_view, name='posto_profile'),
    path('profile-postos/', profile_postos_view, name='profilePostos'),
    path('posto/<int:posto_id>/submit_comment/', submit_comment, name='submit_comment'),
]
