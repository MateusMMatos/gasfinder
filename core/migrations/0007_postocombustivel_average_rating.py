# Generated by Django 5.0.6 on 2024-07-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_comentario_avaliacao_alter_comentario_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='postocombustivel',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]
