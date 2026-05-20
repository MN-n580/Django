from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categorie_all, name='categorie_all'),
    path('categories/ajout/', views.categorie_ajout, name='categorie_ajout'),
    path('categories/traitement/', views.categorie_traitement, name='categorie_traitement'),
    path('categories/read/<int:id>/', views.categorie_read, name='categorie_read'),
    path('categories/update/<int:id>/', views.categorie_update, name='categorie_update'),
    path('categories/traitementupdate/<int:id>/', views.categorie_traitementupdate, name='categorie_traitementupdate'),
    path('categories/delete/<int:id>/', views.categorie_delete, name='categorie_delete'),

    path('', views.sport_all, name='sport_all'),
    path('ajout/', views.sport_ajout, name='sport_ajout'),
    path('traitement/', views.sport_traitement, name='sport_traitement'),
    path('read/<int:id>/', views.sport_read, name='sport_read'),
    path('update/<int:id>/', views.sport_update, name='sport_update'),
    path('traitementupdate/<int:id>/', views.sport_traitementupdate, name='sport_traitementupdate'),
    path('delete/<int:id>/', views.sport_delete, name='sport_delete'),
]