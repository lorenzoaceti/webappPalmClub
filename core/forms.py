from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    celular = forms.IntegerField(label='Cel')
    estado = forms.CharField(label='UF', max_length=2)
    cidade = forms.CharField(label='Cidade', max_length=100)
    sexo = forms.CharField(label='Sexo')
    data = forms.DateField(label='Data')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        celular = self.cleaned_data['celular']
        estado = self.cleaned_data['estado']
        cidade = self.cleaned_data['cidade']
        sexo = self.cleaned_data['sexo']
        data = self.cleaned_data['data']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nCelular: {celular}\nUF: {estado}\n' \
                   f'Cidade: {cidade}\nSexo: {sexo}\nData: {data}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject=nome,
            body=conteudo,
            from_email='contato@palmclub.com.br',
            to=['contato@palmclub.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()
