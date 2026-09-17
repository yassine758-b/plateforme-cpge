from django.db import models


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
