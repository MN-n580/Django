from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LivreForm
from . import models

def ajout(request):
    form_vide = LivreForm()
    return render(request, "bibliotheque/ajout.html", {"form": form_vide})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save()
        return render(request, "bibliotheque/affiche.html", {"Livre": Livre})
    else:
        return render(request, "bibliotheque/ajout.html", {"form": lform})


def all_books(request):
    livres = list(models.Livre.objects.all())
    return render(request, "bibliotheque/all.html", {"livres": livres})


def read(request, id):
    Livre = models.Livre.objects.get(pk=id)
    return render(request, "bibliotheque/affiche.html", {"Livre": Livre})

def update(request, id):
    livre = models.Livre.objects.get(pk=id)
    dictionnaire = {
        'titre': livre.titre,
        'auteur': livre.auteur,
        'date_parution': livre.date_parution,
        'nombre_pages': livre.nombre_pages,
        'resume': livre.resume
    }
    form = LivreForm(initial=dictionnaire)
    return render(request, "bibliotheque/update.html", {"form": form, "id": id})

def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False)
        livre.id = id
        livre.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request, "bibliotheque/update.html", {"form": lform, "id": id})

def delete(request, id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/bibliotheque/")