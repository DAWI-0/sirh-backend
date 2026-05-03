from rest_framework import serializers
from .models import Contrat, Evaluation, FichePaie

class ContratSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrat
        fields = '__all__'

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'

class FichePaieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichePaie
        fields = '__all__'