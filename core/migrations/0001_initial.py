# Generated by Django 3.2.3 on 2021-06-25 11:24

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GaleriaBanheiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='imagem')),
                ('titulo', models.CharField(max_length=1000, verbose_name='titulo')),
            ],
        ),
        migrations.CreateModel(
            name='GaleriaCozinha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='imagem')),
                ('titulo', models.CharField(max_length=1000, verbose_name='titulo')),
            ],
        ),
        migrations.CreateModel(
            name='GaleriaQuartos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='imagem')),
                ('titulo', models.CharField(max_length=1000, verbose_name='titulo')),
            ],
        ),
        migrations.CreateModel(
            name='GaleriaSala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='imagem')),
                ('titulo', models.CharField(max_length=1000, verbose_name='titulo')),
            ],
        ),
        migrations.CreateModel(
            name='ImagemCarrousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='imagem')),
                ('titulo', models.CharField(max_length=200, verbose_name='titulo')),
                ('texto', models.CharField(max_length=1000, verbose_name='texto')),
            ],
        ),
        migrations.CreateModel(
            name='ImagemProjeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='imagem')),
                ('titulo', models.CharField(max_length=1000, verbose_name='titulo')),
            ],
        ),
        migrations.CreateModel(
            name='Texto2Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=10000, verbose_name='Texto')),
            ],
        ),
        migrations.CreateModel(
            name='TextoIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=3000, verbose_name='Titulo')),
                ('Subtexto', models.TextField(max_length=1000000, verbose_name='Texto')),
                ('foto', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='imagem')),
            ],
        ),
        migrations.CreateModel(
            name='TextoSobreNos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=10000, verbose_name='texto')),
                ('TextoNossaMissao', models.CharField(max_length=10000, verbose_name='texto')),
                ('TextoNossaVisao', models.CharField(max_length=10000, verbose_name='texto')),
            ],
        ),
    ]
