from django.shortcuts import render
from .models import Manga, Jeux

# Vue pour lister tous les mangas
def manga_list(request):
    mangas = Manga.objects.all()
    return render(request, 'manga_list.html', {'mangas': mangas})

# Vue pour lister tous les jeux
def jeux_list(request):
    jeux = Jeux.objects.all()
    return render(request, 'jeux_list.html', {'jeux': jeux})
