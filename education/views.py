from django.shortcuts import render
from .models import Niveau, Chapitre, Document
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# NOUVEAU : Page d'inscription pour les élèves
def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Crée l'utilisateur (le ProfilEleve est créé automatiquement grâce à notre code précédent)
            return redirect('login') # Renvoie vers la page de connexion
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# NOUVEAU : Page d'explication pour devenir Premium
@login_required(login_url='login')
def page_abonnement(request):
    return render(request, 'education/abonnement.html')



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