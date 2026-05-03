from django.contrib import admin
from .models import Departement, Projet

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    # list_display définit les colonnes visibles dans la liste
    list_display = ('id', 'nom_departement', 'manager', 'budget_annuel')
    
    # readonly_fields permet d'afficher l'UUID dans la fiche sans qu'il soit modifiable
    readonly_fields = ('id',)
    
    # list_display_links permet de cliquer sur l'ID pour ouvrir la fiche
    list_display_links = ('id', 'nom_departement')

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_projet', 'chef_projet', 'date_limite', 'statut')
    readonly_fields = ('id',)