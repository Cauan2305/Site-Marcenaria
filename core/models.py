from django.db import models
from django.db.models.fields import TextField
from stdimage.models import StdImageField
import uuid

def get_file_path(__instance,filename):
    ext=filename.split('.')[-1]
    filename=f'{uuid.uuid4()}.{ext}'
    return filename



class TextoIndex(models.Model):
     
    titulo=models.CharField('Titulo',max_length=3000)
    Subtexto=models.TextField('Texto',max_length=1000000)
    foto=StdImageField('imagem',upload_to=get_file_path,variations={'thumb':{'width' : 470,'height':600 ,'crop':True}})

class ImagemCarrousel(models.Model):
    imagem=StdImageField('imagem',upload_to=get_file_path,variations={'thumb':{'width' : 442,'height':600 ,'crop':True}})
    titulo=models.CharField('titulo',max_length=200)
    texto=models.CharField('texto',max_length=1000)


class Texto2Index(models.Model):
    texto=TextField('Texto',max_length=10000)

# class ImagemProjeto(models.Model):
#      imagem=StdImageField('imagem',upload_to=get_file_path,variations={'thumb':{'width' : 570,'height':380 ,'crop':True}})
#      titulo=models.CharField('titulo',max_length=1000)
#     #  url=models.URLField('Url')


class TextoSobreNos(models.Model):
    texto=models.CharField('texto',max_length=10000)
    TextoNossaMissao=models.CharField('texto',max_length=10000)
    TextoNossaVisao=models.CharField('texto',max_length=10000)


class GaleriaQuartos(models.Model):
    imagem=StdImageField('imagem',upload_to=get_file_path,variations={'thumb':{'width' : 570,'height':380 ,'crop':True}})
    titulo=models.CharField('titulo',max_length=1000)



class GaleriaSala(models.Model):
    imagem=StdImageField('imagem',upload_to=get_file_path,variations={'thumb':{'width' : 570,'height':380 ,'crop':True}})
    titulo=models.CharField('titulo',max_length=1000)


class GaleriaBanheiro(models.Model):
    imagem=StdImageField('imagem',upload_to=get_file_path,variations={'thumb':{'width' : 570,'height':380 ,'crop':True}})
    titulo=models.CharField('titulo',max_length=1000)

class GaleriaCozinha(models.Model):
    imagem=StdImageField('imagem',upload_to=get_file_path,variations={'thumb':{'width' : 570,'height':380 ,'crop':True}})
    titulo=models.CharField('titulo',max_length=1000)