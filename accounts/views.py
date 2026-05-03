from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Employe, ManagerRH
from .serializers import EmployeSerializer, ManagerRHSerializer
from .permissions import IsAdministrateur, IsAdminOrRH, IsChefDepartementOrRH

class CreateEmployeView(generics.CreateAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [IsAdminOrRH]

class CreateManagerRHView(generics.CreateAPIView):
    queryset = ManagerRH.objects.all()
    serializer_class = ManagerRHSerializer
    permission_classes = [IsAdministrateur]

class EmployeListView(generics.ListAPIView):
    serializer_class = EmployeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        
        if user.role in ['ADMIN', 'RH']:
            return Employe.objects.all()
        
        try:
            employe_connecte = Employe.objects.get(id=user.id)
            if hasattr(employe_connecte, 'departement_dirige'):
                return Employe.objects.filter(departement=employe_connecte.departement_dirige)
            return Employe.objects.filter(id=employe_connecte.id)
        except Employe.DoesNotExist:
            return Employe.objects.none()

class EmployeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [IsChefDepartementOrRH]