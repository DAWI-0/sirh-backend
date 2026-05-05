from django.urls import path
from .views import IoTPontageView, PointageListView

urlpatterns = [
    # Route pour le script Python (POST)
    path('iot/upload/', IoTPontageView.as_view(), name='iot-upload'),
    
    # Route pour React (GET) - AJOUTE BIEN LE SLASH À LA FIN
    path('pointages/', PointageListView.as_view(), name='pointages-list'),
]