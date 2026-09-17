from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('cours/', views.liste_cours, name='liste_cours'),
     path('profil/', views.profil, name='profil'), # <-- NOUVELLE LIGNE
]