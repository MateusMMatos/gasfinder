from django.contrib import admin
from .models import (Cidade, Localizacao, UsuarioProfile, PostoCombustivel, TipoCombustivel, PrecoCombustivel, 
                     FotoVerificacao, Avaliacao, Comentario, Borracharia, OficinaMecanica, Desconto, CodigoDesconto)

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

@admin.register(FotoVerificacao)
class FotoVerificacaoAdmin(admin.ModelAdmin):
    list_display = ['preco', 'data_hora_upload']
    search_fields = ['preco__posto__nome', 'preco__tipo_combustivel__nome']

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'posto', 'nota']
    search_fields = ['usuario__username', 'posto__nome']
    list_filter = ['nota']

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'posto', 'data_hora']
    search_fields = ['usuario__username', 'posto__nome']
    list_filter = ['data_hora']

@admin.register(Borracharia)
class BorrachariaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'localizacao']
    search_fields = ['nome']
    list_filter = ['localizacao__cidade']

@admin.register(OficinaMecanica)
class OficinaMecanicaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'localizacao']
    search_fields = ['nome']
    list_filter = ['localizacao__cidade']

@admin.register(Desconto)
class DescontoAdmin(admin.ModelAdmin):
    list_display = ['posto', 'percentual', 'descricao']
    search_fields = ['posto__nome']
    list_filter = ['posto__localizacao__cidade']

@admin.register(CodigoDesconto)
class CodigoDescontoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'desconto', 'codigo', 'usado']
    search_fields = ['usuario__username', 'codigo']
    list_filter = ['usado']

# Registrando os modelos sem personalização (opcional)
# admin.site.register(Desconto)
# admin.site.register(CodigoDesconto)
