from django.urls import path
from .views import reserver_manga

urlpatterns = [
    path('api/reserver/manga/<int:manga_id>/', reserver_manga, name='reserver_manga'),
]
