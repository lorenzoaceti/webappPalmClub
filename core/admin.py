from django.contrib import admin
from .models import ImagemHome, Evento, Artista


@admin.register(ImagemHome)
class ImagemHomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'ativo', 'modificado')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nomeEvento', 'principal', 'ativo', 'modificado')


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'evento', 'principal', 'ativo', 'modificado')
