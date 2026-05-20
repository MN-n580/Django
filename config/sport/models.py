from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom

class Sport(models.Model):
    nom = models.CharField(max_length=100)
    nb_joueurs = models.IntegerField(blank=False)
    description = models.TextField(null=True, blank=True)

    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__ (self):
        return f"{self.nom} ({self.categorie})"
