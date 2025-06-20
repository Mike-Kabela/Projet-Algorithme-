import os
import sys

# Demande à l'utilisateur d'entrer le chemin du dossier a trier
def demander_chemin_dossier():
    chemin = input("Entrez le chemin du dossier à trier : ").strip()
    
    # Vérifie si le chemin existe et est un dossier
    if not os.path.isdir(chemin):
        print("Erreur : le chemin spécifié n'est pas un dossier valide.")
        sys.exit(1)  # Arrête le programme si le chemin est invalide

    # Retourne le chemin complet, absolu
    return os.path.abspath(chemin)


# Liste tous les fichiers dans le dossier (ignorer les sous-dossiers et fichiers cachés)
def lister_fichiers(chemin):
    fichiers = []
    for nom in os.listdir(chemin):
        chemin_complet = os.path.join(chemin, nom)

        # Vérifie si c'est un fichier (et pas un dossier), et qu’il n’est pas caché (ne commence pas par .)
        if os.path.isfile(chemin_complet) and not nom.startswith("."):
            fichiers.append(chemin_complet)
    return fichiers


# Trie les fichiers selon leur extension
def detecter_extensions(fichiers):
    fichiers_par_extension = {}      # Dictionnaire : extension -> liste de fichiers
    fichiers_sans_extension = []     # Liste des fichiers qui n'ont pas d'extension

    for chemin_fichier in fichiers:
        nom_fichier = os.path.basename(chemin_fichier)

        # Sépare le nom du fichier et son extension
        _, extension = os.path.splitext(nom_fichier)

        # Si le fichier n'a pas d'extension, on l'ajoute à la liste dédiée
        if extension == "":
            fichiers_sans_extension.append(chemin_fichier)
        else:
            extension = extension.lower().strip(".")  # Nettoie l’extension (ex: ".JPG" → "jpg")
            if extension not in fichiers_par_extension:
                fichiers_par_extension[extension] = []
            fichiers_par_extension[extension].append(chemin_fichier)

    return fichiers_par_extension, fichiers_sans_extension
