from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CidadeViewSet, LocalizacaoViewSet, UsuarioViewSet, PostoCombustivelViewSet, TipoCombustivelViewSet,
    PrecoCombustivelViewSet, FotoVerificacaoViewSet, AvaliacaoViewSet, ComentarioViewSet,
    BorrachariaViewSet, OficinaMecanicaViewSet, home_view, discounts_view, register_view,
    login_view, logout_view
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
    path('api/', include(router.urls)),
]
