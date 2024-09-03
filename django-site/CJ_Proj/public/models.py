from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings

class User(AbstractUser):
    badgeur = models.BooleanField(default=False)


class Manga(models.Model):
    caution_livre = models.IntegerField()
    num_tome = models.IntegerField()
    etat_pret_livre = models.BooleanField()
    nom_serie = models.CharField(max_length=50)


class Jeux(models.Model):
    etat_pret_jeu = models.BooleanField()
    nom_jeu = models.CharField(max_length=200)
    caution_jeu = models.IntegerField()


class Pret_CJ(models.Model):
    date_debut_jeu = models.DateTimeField(default=timezone.now)
    date_fin_jeu = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jeu = models.ForeignKey(Jeux, on_delete=models.CASCADE)


class Pret_AnimINT(models.Model):
    date_debut_livre = models.DateTimeField(default=timezone.now)
    date_fin_livre = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    livre = models.ForeignKey(Manga, on_delete=models.CASCADE)