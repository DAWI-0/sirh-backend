from django.urls import path
from .views import DepartementListView

urlpatterns = [
    path('departements/', DepartementListView.as_view(), name='departement-list'),
]