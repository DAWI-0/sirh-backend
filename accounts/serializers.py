import uuid # <-- AJOUT OBLIGATOIRE ICI
from rest_framework import serializers
from .models import Employe, ManagerRH
from organization.models import Departement

class EmployeSerializer(serializers.ModelSerializer):
    departement_nom = serializers.ReadOnlyField(source='departement.nom_departement')
    est_manager = serializers.BooleanField(write_only=True, required=False, default=False)
    matricule = serializers.CharField(required=False, allow_blank=True, validators=[])

    class Meta:
        model = Employe
        fields = ['id', 'username', 'email', 'password', 'matricule', 'poste_titre', 'departement', 'departement_nom', 'matrice_competences', 'role', 'est_manager']
        extra_kwargs = {
            'password': {'write_only': True},
            'matricule': {'required': False} # <-- IMPORTANT : Empêche DRF de bloquer la requête si le matricule est vide depuis React
        }

    def create(self, validated_data):
        # 1. Génération du matricule automatique
        if 'matricule' not in validated_data or not validated_data['matricule']:
            validated_data['matricule'] = f"EMP-{uuid.uuid4().hex[:6].upper()}" # <-- Indentation corrigée
            
        # 2. Extraction des champs spéciaux qui ne vont pas direct dans Employe
        est_manager = validated_data.pop('est_manager', False)
        password = validated_data.pop('password')
        
        # 3. Création et sauvegarde de l'employé
        employe = Employe(**validated_data)
        employe.set_password(password)
        employe.role = 'EMPLOYE'
        employe.save()
        
        # 4. Affectation au rôle de manager du département si la case a été cochée
        if est_manager and employe.departement:
            dept = employe.departement
            dept.manager = employe
            dept.save()
            
        return employe

class ManagerRHSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerRH
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        manager = ManagerRH(**validated_data)
        manager.set_password(password)
        manager.role = 'RH'
        manager.is_staff = True
        manager.save()
        return manager