from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ImagemHome, Evento, Artista
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['imagensHome'] = ImagemHome.objects.all()
        context['qtdImagens'] = range(ImagemHome.objects.count())
        context['primeiraImagem'] = ImagemHome.objects.first()
        context['eventos'] = Evento.objects.all()
        context['artistas'] = Artista.objects.order_by('principal').reverse().all()
        return context

    def form_valid(self, form, *arg, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso.')
        return super(IndexView, self).form_valid(form, *arg, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail.')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
