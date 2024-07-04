# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg, F
from .models import Avaliacao, Comentario, PostoCombustivel, PontuacaoUsuario

@receiver(post_save, sender=Avaliacao)
def atualizar_media_avaliacoes(sender, instance, **kwargs):
    posto = instance.posto
    media_avaliacoes = Avaliacao.objects.filter(posto=posto).aggregate(Avg('nota'))['nota__avg']
    posto.average_rating = media_avaliacoes if media_avaliacoes is not None else 0
    posto.save()

@receiver(post_save, sender=Avaliacao)
def adicionar_pontos_avaliacao(sender, instance, created, **kwargs):
    if created:
        PontuacaoUsuario.objects.filter(usuario=instance.usuario).update(pontos=F('pontos') + 5)

@receiver(post_save, sender=Comentario)
def adicionar_pontos_comentario(sender, instance, created, **kwargs):
    if created:
        PontuacaoUsuario.objects.filter(usuario=instance.usuario).update(pontos=F('pontos') + 3)
