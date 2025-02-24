from rest_framework import serializers
from .models import (
    Cidade, Localizacao, UsuarioProfile, PostoCombustivel, TipoCombustivel,
    PrecoCombustivel, Avaliacao, Comentario
)

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioProfile
        fields = '__all__'

class PostoCombustivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostoCombustivel
        fields = '__all__'

class TipoCombustivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCombustivel
        fields = '__all__'

class PrecoCombustivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecoCombustivel
        fields = '__all__'

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
