import uuid
from django.db import models

class PointageIoT(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employe = models.ForeignKey('accounts.Employe', on_delete=models.CASCADE, related_name='pointages')
    timestamp = models.DateTimeField()
    id_capteur = models.CharField(max_length=50)
    est_justifie = models.BooleanField(default=False)

    def __str__(self):
        return f"Pointage - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

class DemandeConge(models.Model):
    STATUT_CHOICES = [
        ('ATTENTE', 'En attente'),
        ('VALIDE', 'Validé'),
        ('REFUSE', 'Refusé'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employe = models.ForeignKey('accounts.Employe', on_delete=models.CASCADE, related_name='conges')
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='ATTENTE')
    motif = models.TextField()

    def __str__(self):
        return f"Congé - {self.statut}"