from django.contrib import admin
from .models import Cidade, Localizacao, UsuarioProfile, PostoCombustivel, TipoCombustivel, PrecoCombustivel, FotoVerificacao, Avaliacao, Comentario, Borracharia, OficinaMecanica

admin.site.register(Cidade)
admin.site.register(Localizacao)
admin.site.register(UsuarioProfile)
admin.site.register(PostoCombustivel)
admin.site.register(TipoCombustivel)
admin.site.register(PrecoCombustivel)
admin.site.register(FotoVerificacao)
admin.site.register(Avaliacao)
admin.site.register(Comentario)
admin.site.register(Borracharia)
admin.site.register(OficinaMecanica)
