from django.contrib import admin
from .models import (
    Cidade, Localizacao, UsuarioProfile, PostoCombustivel, TipoCombustivel, PrecoCombustivel, 
    Avaliacao, Comentario, HistoricoAbastecimento
)

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'estado', 'pais']
    search_fields = ['nome', 'estado', 'pais']

@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ['endereco', 'cidade', 'latitude', 'longitude']
    search_fields = ['endereco', 'cidade__nome']
    list_filter = ['cidade__estado']

@admin.register(UsuarioProfile)
class UsuarioProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'data_cadastro', 'localizacao']
    search_fields = ['user__username']
    list_filter = ['data_cadastro']

@admin.register(PostoCombustivel)
class PostoCombustivelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj', 'localizacao']
    search_fields = ['nome', 'cnpj']
    list_filter = ['localizacao__cidade']

@admin.register(TipoCombustivel)
class TipoCombustivelAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(PrecoCombustivel)
class PrecoCombustivelAdmin(admin.ModelAdmin):
    list_display = ['posto', 'tipo_combustivel', 'valor', 'data_atualizacao']
    search_fields = ['posto__nome', 'tipo_combustivel__nome']
    list_filter = ['data_atualizacao', 'posto__localizacao__cidade']

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'nota', 'posto']
    search_fields = ['usuario__username', 'posto__nome']
    list_filter = ['nota']

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'posto', 'data_hora']
    search_fields = ['usuario__username', 'posto__nome']
    list_filter = ['data_hora']

@admin.register(HistoricoAbastecimento)
class HistoricoAbastecimentoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'posto', 'preco_combustivel', 'data_hora']
    search_fields = ['usuario__username', 'posto__nome']
    list_filter = ['data_hora']
