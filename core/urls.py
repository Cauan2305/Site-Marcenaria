from django.urls import path,include
from django.urls.conf import re_path
from .views import IndexView,ContatoView,ProjetosView,SobreView,QuartoView,CozinhaView,SalaView,BanheiroView

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('projetos/',ProjetosView.as_view(),name='projeto'),
    path('contato/',ContatoView.as_view(),name='contato'),
    path('sobre/',SobreView.as_view(),name='sobre'),
    re_path(r'^quarto/',QuartoView.as_view(),name='quarto'),
    re_path(r'^cozinha/',CozinhaView.as_view(),name='cozinha'),
    re_path(r'^sala/',SalaView.as_view(),name='sala'),
    re_path(r'^banheiro/',BanheiroView.as_view(),name='banheiro'),


]