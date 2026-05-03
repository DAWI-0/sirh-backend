from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Departement
from .serializers import DepartementSerializer

class DepartementListView(generics.ListAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    permission_classes = [IsAuthenticated] # Seul un utilisateur connecté peut voir les départements