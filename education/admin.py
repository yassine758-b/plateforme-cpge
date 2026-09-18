from django.contrib import admin
from .models import Niveau, Chapitre, Document
from .models import ProfilEleve

class DocumentAdmin(admin.ModelAdmin):
    # On ajoute 'est_publie' dans l'affichage
    list_display = ('titre', 'type_document', 'chapitre', 'est_publie', 'date_ajout', 'est_prive')
    
    # On permet de filtrer par statut (Publié ou Brouillon)
    list_filter = ('est_publie', 'type_document', 'chapitre__niveau')
    
    # On ajoute une barre de recherche
    search_fields = ('titre',)
    
    # ASTUCE : Permet au prof de cocher/décocher directement dans la liste !
    list_editable = ('est_publie','est_prive')

class ChapitreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'niveau')
    list_filter = ('niveau',)

admin.site.register(Niveau)
admin.site.register(Chapitre, ChapitreAdmin)
admin.site.register(Document, DocumentAdmin)

@admin.register(ProfilEleve)
class ProfilEleveAdmin(admin.ModelAdmin):
    list_display = ('user', 'est_premium', 'date_fin_abonnement')
    list_filter = ('est_premium',)
    search_fields = ('user__username',)
    list_editable = ('est_premium',) # Permet au prof de cocher la case directement depuis la liste !