from rest_framework import serializers
from .models import PointageIoT
from accounts.models import Employe

class PointageIoTSerializer(serializers.ModelSerializer):
    # 1. On mappe le champ 'employe' au matricule pour la création
    employe = serializers.SlugRelatedField(
        queryset=Employe.objects.all(),
        slug_field='matricule'
    )
    
    # 2. Champs de lecture seule pour l'affichage React
    employe_nom = serializers.ReadOnlyField(source='employe.username')
    matricule_display = serializers.ReadOnlyField(source='employe.matricule')

    class Meta:
        model = PointageIoT
        fields = [
            'id', 
            'employe', 
            'employe_nom', 
            'matricule_display', 
            'type_pointage', 
            'timestamp', 
            'id_capteur', 
            'est_justifie'
        ]

    # Pas besoin de def create() personnalisé ici, le ModelSerializer 
    # gère déjà tout automatiquement une fois que SlugRelatedField est configuré.