from rest_framework import serializers
from .models import Employe, ManagerRH
from organization.models import Departement

class EmployeSerializer(serializers.ModelSerializer):
    departement_nom = serializers.ReadOnlyField(source='departement.nom_departement')
    est_manager = serializers.BooleanField(write_only=True, required=False, default=False)

    class Meta:
        model = Employe
        fields = ['id', 'username', 'email', 'password', 'matricule', 'poste_titre', 'departement', 'departement_nom', 'matrice_competences', 'role', 'est_manager']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        est_manager = validated_data.pop('est_manager', False)
        password = validated_data.pop('password')
        
        employe = Employe(**validated_data)
        employe.set_password(password)
        employe.role = 'EMPLOYE'
        employe.save()
        
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