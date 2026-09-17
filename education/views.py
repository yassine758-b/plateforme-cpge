from django.shortcuts import render
from .models import Niveau, Chapitre, Document
from django.contrib.auth.decorators import login_required
def accueil(request):
    return render(request, 'education/accueil.html')

# --- NOUVELLE FONCTION À AJOUTER ---
def liste_cours(request):
    # On récupère tous les niveaux dans la base de données
    niveaux = Niveau.objects.all()
    # On envoie ces données à un nouveau template nommé 'cours.html'
    return render(request, 'education/cours.html', {'niveaux': niveaux})

@login_required(login_url='login')
def profil(request):
    # On peut envoyer des statistiques à l'élève pour le motiver
    nb_docs_prives = Document.objects.filter(est_prive=True, est_publie=True).count()
    
    return render(request, 'education/profil.html', {
        'nb_docs_prives': nb_docs_prives
    })