import uuid
from django.db import models

class Departement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom_departement = models.CharField(max_length=100)
    budget_annuel = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    manager = models.OneToOneField(
        'accounts.Employe', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='departement_dirige'
    )

    def __str__(self):
        return self.nom_departement

class Projet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom_projet = models.CharField(max_length=100)
    date_limite = models.DateField()
    statut = models.CharField(max_length=50, default='En cours')
    
    chef_projet = models.ForeignKey(
        'accounts.Employe', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='projets_diriges'
    )
    
    equipe = models.ManyToManyField(
        'accounts.Employe', 
        related_name='projets_affectes', 
        blank=True
    )

    def __str__(self):
        return self.nom_projet