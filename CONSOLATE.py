import os
import shutil
import re
from datetime import datetime

# Répertoire à organiser
SOURCE_DIR = "fichiers_a_organiser"
DEST_DIR = "organised_files "

def nettoyer_nom_fichier(nom) :
    nom = nom.strip()
    nom = re.sub(r'[^\w\-_.]' , '_', nom)
    return nom

def generer_nom_unique(dossier, nom_fichier) :
    base, ext = os.path.splitext(nom_fichier)
    Compteur = 1
    nouveau_nom = nom_fichier

    while os.path.exists(os.path.join(dossier, nouveau_nom)) :
        nouveau_nom = f"{base}_{compteur}{ext}"
        compteur += 1

    return nouveau_nom

def organiser_fichiers() :
    if not os.path.exists(SOURCE_DIR) :
        print(f"Le dossier source '{SOURCE_DIR}' n’existe pas.")
        return

    os.makedirs(DEST_DIR, exist_ok = True)

    for nom_fichier in os.listdir(SOURCE_DIR) :
        chemin_complet = os.path.join(SOURCE_DIR, nom_fichier)

    if os.path.isfile(chemin_complet) :
            nom_propre = nettoyer_nom_fichier(nom_fichier)
            extension = os.path.splitext(nom_propre)[1][1 :].lower() or "autres"
            dossier_cible = os.path.join(DEST_DIR, extension)
            os.makedirs(dossier_cible, exist_ok=True)

            nom_final = generer_nom_unique(dossier_cible, nom_propre)
            chemin_cible = os.path.join(dossier_cible, nosm_final)

            shutil.move(chemin_complet, chemin_cible)
            print(f"Déplacé : {nom_fichier} → {chemin_cible} ")

if __name__ == "__main__" :
    organiser_fichiers()
