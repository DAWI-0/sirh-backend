from rest_framework import serializers
from .models import Departement

class DepartementSerializer(serializers.ModelSerializer):
    # On peut ajouter un champ pour compter les employés plus tard
    class Meta:
        model = Departement
        fields = '__all__'