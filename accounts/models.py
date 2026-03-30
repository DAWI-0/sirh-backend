import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Le modèle parent (Sécurité et Rôles)
class Utilisateur(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    ROLE_CHOICES = [
        ('ADMIN', 'Administrateur'),
        ('RH', 'Manager RH'),
        ('EMPLOYE', 'Employé'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='EMPLOYE')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


# 2. Le modèle Employé
class Employe(Utilisateur):
    matricule = models.CharField(max_length=50, unique=True)
    solde_conges = models.FloatField(default=22.5)
    poste_titre = models.CharField(max_length=100)
    matrice_competences = models.JSONField(default=list, blank=True, null=True)
    
    # La magie du multi-applications : on pointe vers l'app "organization" !
    departement = models.ForeignKey(
        'organization.Departement', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='employes'
    )

    class Meta:
        verbose_name = "Employé"
        verbose_name_plural = "Employés"


# 3. Les Proxy Models (Pour respecter l'UML)
class ManagerRH(Utilisateur):
    class Meta:
        proxy = True
        verbose_name = "Manager RH"
        verbose_name_plural = "Managers RH"

class Administrateur(Utilisateur):
    class Meta:
        proxy = True
        verbose_name = "Administrateur"
        verbose_name_plural = "Administrateurs"