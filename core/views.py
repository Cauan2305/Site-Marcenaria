from django.views.generic import TemplateView,FormView
from .forms import ContatoForms
from django.urls import reverse_lazy
from django.contrib import messages
from .models import TextoIndex,ImagemCarrousel,Texto2Index,GaleriaSala,GaleriaQuartos,GaleriaCozinha,GaleriaBanheiro,TextoSobreNos

class IndexView (TemplateView):
    template_name='index.html'
    def get_context_data(self, *args,**kwargs):
        context=super(IndexView,self).get_context_data(**kwargs)
        context={
            'TextoIndex':TextoIndex.objects.all(),
            'ImagemCarrousel':ImagemCarrousel.objects.all() ,
            'Texto2index':Texto2Index.objects.all(),
            'TextoSobreNos':TextoSobreNos.objects.all(),

        }
        return context
    
class ContatoView(FormView):
    template_name='contato.html'
    form_class=ContatoForms
    success_url=reverse_lazy('contato')
    

    def form_valid(self, form,*args,**kwargs) :
        # form.send_email()
        messages.success(self.request,'Email Enviado com sucesso')
        return super(ContatoView,self).form_valid(form,*args,**kwargs)


    def form_invalid(self, form,*args,**kwargs):
        form.send_email()
        messages.error(self.request,'Erro ao Enviar o Email')
        return super(ContatoView,self).form_invalid(form,*args,**kwargs)



class ProjetosView(TemplateView):
    template_name='projects.html'

class SobreView (TemplateView):
    template_name='about.html'
    def get_context_data(self, *args,**kwargs):
        context=super(SobreView,self).get_context_data(**kwargs) 
        context={
            'TextoSobreNos':TextoSobreNos.objects.all(),
            

        }
        return context

class QuartoView (TemplateView):
    template_name='quarto.html'
    def get_context_data(self, *args,**kwargs):
        context=super(QuartoView,self).get_context_data(**kwargs) 
        context={
            'GaleriaQuarto':GaleriaQuartos.objects.all(),
            

        }
        return context

class CozinhaView (TemplateView):
    template_name='cozinha.html'
    def get_context_data(self, *args,**kwargs):
        context=super(CozinhaView,self).get_context_data(**kwargs) 
        context={
            'GaleriaCozinha':GaleriaCozinha.objects.all(),
            

        }
        return context
class SalaView (TemplateView):
    template_name='sala.html'

    def get_context_data(self, *args,**kwargs):
        context=super(SalaView,self).get_context_data(**kwargs) 
        context={
            'GaleriaSala':GaleriaSala.objects.all(),
            

        }
        return context
    

class BanheiroView (TemplateView):
    template_name='banheiro.html'
    def get_context_data(self, *args,**kwargs):
        context=super(BanheiroView,self).get_context_data(**kwargs) 
        context={
            'GaleriaBanheiro':GaleriaBanheiro.objects.all(),
            

        }
        return context
    