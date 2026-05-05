from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Departement
from .serializers import DepartementSerializer

class DepartementViewSet(viewsets.ModelViewSet):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    permission_classes = [IsAuthenticated]