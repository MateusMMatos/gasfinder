from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F
from .models import FotoVerificacao, Avaliacao, Comentario, PontuacaoUsuario

@receiver(post_save, sender=FotoVerificacao)
def adicionar_pontos(sender, instance, created, **kwargs):
    if created:
        PontuacaoUsuario.objects.filter(usuario=instance.usuario).update(pontos=F('pontos') + 10)

@receiver(post_save, sender=Avaliacao)
def adicionar_pontos_avaliacao(sender, instance, created, **kwargs):
    if created:
        PontuacaoUsuario.objects.filter(usuario=instance.usuario).update(pontos=F('pontos') + 5)

@receiver(post_save, sender=Comentario)
def adicionar_pontos_comentario(sender, instance, created, **kwargs):
    if created:
        PontuacaoUsuario.objects.filter(usuario=instance.usuario).update(pontos=F('pontos') + 3)
