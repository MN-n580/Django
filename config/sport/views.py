from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CategorieForm, SportForm
from . import models


# ===================== CATEGORIE =====================

def categorie_all(request):
    categories = list(models.Categorie.objects.all())
    sports = list(models.Sport.objects.all())
    return render(request, "sport/categorie_all.html", {"categories": categories, "sports": sports})

def categorie_ajout(request):
    form = CategorieForm()
    return render(request, "sport/categorie_ajout.html", {"form": form})

def categorie_traitement(request):
    form = CategorieForm(request.POST)
    if form.is_valid():
        categorie = form.save()
        return render(request, "sport/categorie_affiche.html", {"categorie": categorie})
    else:
        return render(request, "sport/categorie_ajout.html", {"form": form})

def categorie_read(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    return render(request, "sport/categorie_affiche.html", {"categorie": categorie})

def categorie_update(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    form = CategorieForm({
        'nom': categorie.nom,
        'description': categorie.description,
    })
    return render(request, "sport/categorie_update.html", {"form": form, "id": id})

def categorie_traitementupdate(request, id):
    form = CategorieForm(request.POST)
    if form.is_valid():
        categorie = form.save(commit=False)
        categorie.id = id
        categorie.save()
        return HttpResponseRedirect("/sport/categories/")
    else:
        return render(request, "sport/categorie_update.html", {"form": form, "id": id})

def categorie_delete(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect("/sport/categories/")


# ===================== SPORT =====================

def sport_all(request):
    sports = list(models.Sport.objects.all())
    return render(request, "sport/sport_all.html", {"sports": sports})

def sport_ajout(request):
    form = SportForm()
    return render(request, "sport/sport_ajout.html", {"form": form})

def sport_traitement(request):
    form = SportForm(request.POST)
    if form.is_valid():
        sport = form.save()
        return HttpResponseRedirect("/sport/")
    else:
        return render(request, "sport/sport_ajout.html", {"form": form})

def sport_read(request, id):
    sport = models.Sport.objects.get(pk=id)
    return render(request, "sport/sport_affiche.html", {"sport": sport})

def sport_update(request, id):
    sport = models.Sport.objects.get(pk=id)
    form = SportForm({
        'nom': sport.nom,
        'nb_joueurs': sport.nb_joueurs,
        'description': sport.description,
        'categorie': sport.categorie_id,
    })
    return render(request, "sport/sport_update.html", {"form": form, "id": id})

def sport_traitementupdate(request, id):
    form = SportForm(request.POST)
    if form.is_valid():
        sport = form.save(commit=False)
        sport.id = id
        sport.save()
        return HttpResponseRedirect("/sport/")
    else:
        return render(request, "sport/sport_update.html", {"form": form, "id": id})

def sport_delete(request, id):
    sport = models.Sport.objects.get(pk=id)
    sport.delete()
    return HttpResponseRedirect("/sport/")