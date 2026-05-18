from django.db import models # [cite: 24]

class Livre(models.Model): # Inherits from Django's base Model class [cite: 25]
    titre = models.CharField(max_length=100) # Text field, max 100 characters [cite: 26, 27]
    auteur = models.CharField(max_length=100) # [cite: 27]
    date_parution = models.DateField(blank=True, null=True) # Date, allowed to be empty [cite: 28]
    nombre_pages = models.IntegerField(blank=False) # Mandatory integer field [cite: 29]
    resume = models.TextField(null=True, blank=True) # Long text field [cite: 30]

    def __str__(self): # [cite: 31]
        chaine = f"{self.titre} écrit par {self.auteur} édité le {self.date_parution}" # [cite: 32]
        return chaine # [cite: 32]