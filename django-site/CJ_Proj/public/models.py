from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    badgeur = models.BooleanField(default=False)

class Manga(models.Model):
    caution_livre = models.IntegerField()
    num_tome = models.IntegerField()
    etat_pret_livre = models.BooleanField()
    nom_serie = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom_serie} - Tome {self.num_tome}"

class Jeux(models.Model):
    etat_pret_jeu = models.BooleanField()
    nom_jeu = models.CharField(max_length=200)
    caution_jeu = models.IntegerField()

    def __str__(self):
        return self.nom_jeu

class PretCJ(models.Model):
    date_debut_jeu = models.DateTimeField(default=timezone.now)
    date_fin_jeu = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jeu = models.ForeignKey(Jeux, on_delete=models.CASCADE)

    def __str__(self):
        return f"Prêt du jeu {self.jeu.nom_jeu} à {self.user.username} du {self.date_debut_jeu} au {self.date_fin_jeu}"

    class Meta:
        unique_together = ('user', 'jeu')

class PretAnimInt(models.Model):
    date_debut_livre = models.DateTimeField(default=timezone.now)
    date_fin_livre = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    livre = models.ForeignKey(Manga, on_delete=models.CASCADE)

    def __str__(self):
        return f"Prêt du manga {self.livre.nom_serie} Tome {self.livre.num_tome} à {self.user.username} du {self.date_debut_livre} au {self.date_fin_livre}"

    class Meta:
        unique_together = ('user', 'livre')
