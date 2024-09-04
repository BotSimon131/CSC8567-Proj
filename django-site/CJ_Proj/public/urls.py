from django.urls import path
from . import views

urlpatterns = [
    path('mangas/', views.manga_list, name='manga_list'),
    path('jeux/', views.jeux_list, name='jeux_list'),
]
