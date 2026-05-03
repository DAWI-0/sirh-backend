import os
import django

# 1. Configurer l'environnement Django
# Remplace 'core' par le nom du dossier où se trouve ton fichier settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') 
django.setup()

from organization.models import Departement

def populate_departments():
    # Liste complète des départements
    DEPARTMENTS_LIST = [
        "Direction Générale",
        "Informatique & SI",
        "Ressources Humaines",
        "Finance & Comptabilité",
        "Marketing & Communication",
        "Ventes & Commercial",
        "Logistique & Achats",
        "Recherche & Développement",
        "Juridique & Conformité",
        "Services Généraux"
    ]

    print("--- Début du peuplement des départements ---")

    for name in DEPARTMENTS_LIST:
        obj, created = Departement.objects.get_or_create(nom_departement=name)
        if created:
            print(f"✅ Créé : {name}")
        else:
            print(f"🟡 Existe déjà : {name}")

    print("--- Opération terminée ---")

if __name__ == "__main__":
    populate_departments()