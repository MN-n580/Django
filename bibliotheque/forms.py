from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class LivreForm(ModelForm):
    class Meta:
        model = models.Livre  # Here, we directly link the form to your database blueprint
        fields = ('titre', 'auteur', 'date_parution', 'nombre_pages',
                  'resume')  # The exact columns we want the user to fill

        # Labels are simply the user-friendly text that will appear next to the HTML inputs
        labels = {
            'titre': _('Titre'),
            'auteur': _('Auteur'),
            'date_parution': _('Date de parution'),
            'nombre_pages': _('Nombres de pages'),
            'resume': _('Résumé')
        }