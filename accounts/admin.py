from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur, Employe, ManagerRH, Administrateur

# Pour que l'admin affiche bien nos champs personnalisés
@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('username', 'matricule', 'role', 'poste_titre', 'is_staff')
    search_fields = ('username', 'matricule', 'email')

admin.site.register(Utilisateur)
admin.site.register(ManagerRH)
admin.site.register(Administrateur)