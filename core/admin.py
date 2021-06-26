from django.contrib import admin
from django.db import models
from .models import TextoIndex,ImagemCarrousel,Texto2Index,TextoSobreNos,GaleriaSala,GaleriaBanheiro,GaleriaCozinha,GaleriaQuartos


@admin.register(TextoIndex)
class TextoIndexAdmin(admin.ModelAdmin):
    list_display=('titulo',)


@admin.register(ImagemCarrousel)
class ImagemAdmin(admin.ModelAdmin):
    list_display=('titulo',)

@admin.register(Texto2Index)
class Texto2Admin(admin.ModelAdmin):
    list_display=('texto',)


@admin.register(GaleriaBanheiro)
class GaleriaBanheiroAdmin(admin.ModelAdmin):
    list_display=('titulo',)


@admin.register(GaleriaSala)
class GaleriaSalaAdmin(admin.ModelAdmin):
    list_display=('titulo',)

@admin.register(GaleriaQuartos)
class GaleriaQuartosAdmin(admin.ModelAdmin):
    list_display=('titulo',)

@admin.register(GaleriaCozinha)
class GaleriaCozinhaAdmin(admin.ModelAdmin):
    list_display=('titulo',)

@admin.register(TextoSobreNos)
class SobreNosAdmin(admin.ModelAdmin):
    list_display=('texto',)