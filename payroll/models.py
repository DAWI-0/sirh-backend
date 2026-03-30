import uuid
from django.db import models

class Contrat(models.Model):
    TYPE_CHOICES = [('CDI', 'CDI'), ('CDD', 'CDD'), ('STAGE', 'Stage')]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employe = models.ForeignKey('accounts.Employe', on_delete=models.CASCADE, related_name='contrats')
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    type_contrat = models.CharField(max_length=20, choices=TYPE_CHOICES)
    salaire_mensuel = models.DecimalField(max_digits=10, decimal_places=2)
    jours_preavis = models.IntegerField(default=30)

    def __str__(self):
        return f"Contrat {self.type_contrat}"

class Evaluation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employe = models.ForeignKey('accounts.Employe', on_delete=models.CASCADE, related_name='evaluations')
    date_evaluation = models.DateField()
    note_comportementale = models.FloatField()
    commentaire = models.TextField(blank=True, null=True)

class FichePaie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employe = models.ForeignKey('accounts.Employe', on_delete=models.CASCADE, related_name='fiches_paie')
    periode_mois = models.IntegerField()
    periode_annee = models.IntegerField()
    salaire_base = models.DecimalField(max_digits=10, decimal_places=2)
    deductions_absences = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    primes_evaluation = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    net_a_payer = models.DecimalField(max_digits=10, decimal_places=2)