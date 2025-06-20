import os
import shutil
import re

# Nettoie un nom de fichier : enlève les caractères spéciaux, remplace les espaces par des _
def nettoyer_nom_fichier(nom):
    nom_sans_extension, extension = os.path.splitext(nom)
    
    # Enlève tous les caractères non alphanumériques sauf _ et -
    nom_nettoye = re.sub(r'[^\w\-]', '_', nom_sans_extension)

    # Recompose le nom complet avec l'extension
    return nom_nettoye + extension.lower()


# Vérifie s'il y a un conflit de nom et ajoute un suffixe si nécessaire
def resoudre_conflit(chemin_destination):
    if not os.path.exists(chemin_destination):
        return chemin_destination  # Aucun conflit

    base, extension = os.path.splitext(chemin_destination)
    compteur = 1

    # Ajoute un suffixe (1), (2), etc. jusqu'à trouver un nom disponible
    while True:
        nouveau_chemin = f"{base}({compteur}){extension}"
        if not os.path.exists(nouveau_chemin):
            return nouveau_chemin
        compteur += 1


# Crée le dossier de destination s'il n'existe pas
def creer_dossier_destination(chemin_dossier, nom_dossier):
    dossier = os.path.join(chemin_dossier, nom_dossier.upper())
    if not os.path.exists(dossier):
        os.makedirs(dossier)  # Crée le dossier (et ses parents si besoin)
    return dossier


# Déplace un fichier vers le bon dossier après nettoyage et gestion des doublons
def deplacer_fichier(chemin_fichier, dossier_destination):
    nom_fichier = os.path.basename(chemin_fichier)

    # Nettoyer le nom
    nom_nettoye = nettoyer_nom_fichier(nom_fichier)

    # Chemin de destination
    chemin_destination = os.path.join(dossier_destination, nom_nettoye)

    # Gérer les doublons
    chemin_final = resoudre_conflit(chemin_destination)

    # Déplacer le fichier
    shutil.move(chemin_fichier, chemin_final)

    return chemin_final  # Pour journaliser
