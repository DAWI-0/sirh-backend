from django.urls import path
from .views import ContratListCreateView, EvaluationListCreateView, FichePaieListCreateView

urlpatterns = [
    path('contrats/', ContratListCreateView.as_view(), name='contrat-list'),
    path('evaluations/', EvaluationListCreateView.as_view(), name='evaluation-list'),
    path('fiches/', FichePaieListCreateView.as_view(), name='fichepaie-list'),
]