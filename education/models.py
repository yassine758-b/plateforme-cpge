from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Niveau(models.Model):
    nom = models.CharField(max_length=50) # ex: MPSI, PCSI, MP...
    
    def __str__(self):
        return self.nom

class Chapitre(models.Model):
    titre = models.CharField(max_length=200) # ex: Algèbre linéaire, Topologie...
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE, related_name='chapitres')
    
    def __str__(self):
        return f"{self.titre} ({self.niveau.nom})"

class Document(models.Model):
    TYPES = [
        ('COURS', 'Cours'),
        ('EXO', 'Exercices'),
        ('DS', 'Devoir Surveillé'),
        ('CNC', 'Sujet CNC'),
        ('RES', 'Résumé'),
    ]
    
    titre = models.CharField(max_length=200)
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE, related_name='documents')
    type_document = models.CharField(max_length=5, choices=TYPES)
    fichier = models.FileField(upload_to='documents_maths/')
    date_ajout = models.DateTimeField(auto_now_add=True)

    est_publie = models.BooleanField(default=False, verbose_name="Publier (Visible par les élèves)")
    est_prive = models.BooleanField(default=True, verbose_name="🔒 Réservé aux abonnés")
    
    def __str__(self):
        return f"[{self.get_type_document_display()}] {self.titre}"


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ProfilEleve(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    est_premium = models.BooleanField(default=False, verbose_name="Abonnement Premium Actif")
    date_fin_abonnement = models.DateField(null=True, blank=True, verbose_name="Fin d'abonnement")

    def __str__(self):
        return f"Profil de {self.user.username} - {'Premium' if self.est_premium else 'Gratuit'}"

@receiver(post_save, sender=User)
def creer_profil_eleve(sender, instance, created, **kwargs):
    if created:
        ProfilEleve.objects.create(user=instance)

@receiver(post_save, sender=User)
def sauvegarder_profil_eleve(sender, instance, **kwargs):
    instance.profil.save()