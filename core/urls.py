from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CidadeViewSet, LocalizacaoViewSet, UsuarioViewSet, PostoCombustivelViewSet,
    TipoCombustivelViewSet, PrecoCombustivelViewSet, FotoVerificacaoViewSet,
    AvaliacaoViewSet, ComentarioViewSet, BorrachariaViewSet, OficinaMecanicaViewSet
)

router = DefaultRouter()
router.register(r'cidades', CidadeViewSet)
router.register(r'localizacoes', LocalizacaoViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'postos', PostoCombustivelViewSet)
router.register(r'tipos_combustivel', TipoCombustivelViewSet)
router.register(r'precos_combustivel', PrecoCombustivelViewSet)
router.register(r'fotos_verificacao', FotoVerificacaoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'borracharias', BorrachariaViewSet)
router.register(r'oficinas_mecanicas', OficinaMecanicaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
