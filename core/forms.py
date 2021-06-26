from django import forms
from django.core.mail.message import EmailMessage

class ContatoForms(forms.Form):
    nome=forms.CharField(label='Nome',max_length=100,)
    email=forms.EmailField(label='E-mail',max_length=100)
    # numero=forms.DecimalField(max_digits=8,decimal_places=0)
    mensagem=forms.CharField(label='Mensagem',widget=forms.Textarea())



    def send_email(self):
        nome=self.cleaned_data['nome']
        email=self.cleaned_data['email']
        # numero=self.cleaned_data['numero']
        mensagem=self.cleaned_data['mensagem']

    conteudo=f'Nome {nome} \n E-mail {email}\n Mensagem : {mensagem}\n'
    
    mail=EmailMessage(
        subject=mensagem,
        body=conteudo,
        from_email='cauanmatheustrigo68@gmail.com',
        to=['cauanmatheustrigo68@gmail.com',],
        headers={'Reply-To':email}
        

    )
    
    mail.send()