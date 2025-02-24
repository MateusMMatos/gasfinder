# Generated by Django 5.0.6 on 2024-06-20 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCombustivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('endereco', models.CharField(max_length=255)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Borracharia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('localizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.localizacao')),
            ],
        ),
        migrations.CreateModel(
            name='OficinaMecanica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('localizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.localizacao')),
            ],
        ),
        migrations.CreateModel(
            name='PostoCombustivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=20, unique=True)),
                ('localizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.localizacao')),
            ],
        ),
        migrations.CreateModel(
            name='PrecoCombustivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('posto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.postocombustivel')),
                ('tipo_combustivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipocombustivel')),
            ],
        ),
        migrations.CreateModel(
            name='FotoVerificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caminho_arquivo', models.CharField(max_length=255)),
                ('data_hora_upload', models.DateTimeField(auto_now_add=True)),
                ('preco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.precocombustivel')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('localizacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.localizacao')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('posto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.postocombustivel')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField()),
                ('comentario', models.TextField(blank=True, null=True)),
                ('posto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.postocombustivel')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
    ]
