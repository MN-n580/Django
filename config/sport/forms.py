from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class CategorieForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ('nom', 'description')
        labels = {
            'nom': _('Nom'),
            'description': _('Description'),
        }

class SportForm(ModelForm):
    class Meta:
        model = models.Sport
        fields = ('nom', 'nb_joueurs', 'description', 'categorie')
        labels = {
            'nom': _('Nom du sport'),
            'nb_joueurs': _('Nombre de joueurs'),
            'description': _('Description'),
            'categorie': _('Catégorie'),
        }