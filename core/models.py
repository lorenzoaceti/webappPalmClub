import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class ImagemHome(Base):
    id = models.IntegerField('ID', primary_key=True)
    imagem = StdImageField('Imagem', upload_to=get_file_path,
                           variations={'thumb': {'width': 2048, 'height': 1365, 'crop': True}})

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __int__(self):
        return self.id


class Evento(Base):
    nomeEvento = models.CharField('Nome do Evento', max_length=100)
    dataEvento = models.CharField('Data do Evento', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path)
    principal = models.BooleanField('Evento Principal?', default=False)

    if principal:
        descricao = models.TextField('Descrição', max_length=300, blank=True)
        link = models.CharField('Link pra compra', max_length=100, blank=True, default='#')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.nomeEvento


class Artista(Base):
    SIDE_CHOICES = (
        ('Esquerda', 'Esquerda'),
        ('Direita', 'Direita')
    )

    nome = models.CharField('Nome', max_length=100)
    evento = models.ForeignKey('core.Evento', verbose_name='Evento', on_delete=models.CASCADE)
    principal = models.BooleanField('Artista Principal do Evento?', default=False)
    posicao = models.CharField('Posição no card do evento', max_length=8, choices=SIDE_CHOICES)

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'

    def __str__(self):
        return self.nome






