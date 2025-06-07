import os

def saisir_chemin():
    """ Saisie et validation du chemin du dossier source. """
    chemin = input("Entrez le chemin du dossier source : ")
    while not os.path.isdir(chemin):
        print("Chemin invalide. Veuillez réessayer.")
        chemin = input("Entrez le chemin du dossier source : ")
    return chemin

def lister_fichiers(chemin, ignorer_caches=True):
    """ Liste les fichiers, en ignorant les fichiers cachés si demandé. """
    fichiers = []
    for fichier in os.listdir(chemin):
        chemin_complet = os.path.join(chemin, fichier)
        if os.path.isfile(chemin_complet):
            if ignorer_caches and fichier.startswith('.'):
                continue
            fichiers.append(fichier)
    return fichiers

def identifier_extensions(fichiers):
    """ Identifie et classe les fichiers par extension. """
    extensions = {}
    fichiers_sans_extension = []

    for fichier in fichiers:
        nom, ext = os.path.splitext(fichier)
        ext = ext.lower()
        if ext:
            extensions.setdefault(ext, []).append(fichier)
        else:
            fichiers_sans_extension.append(fichier)

    return extensions, fichiers_sans_extension

def main():
    chemin = saisir_chemin()
    fichiers = lister_fichiers(chemin)
    extensions, fichiers_sans_extension = identifier_extensions(fichiers)

    print("\nFichiers par extension:")
    for ext, fichiers in extensions.items():
        print(f"{ext}: {', '.join(fichiers)}")

    print("\nFichiers sans extension:")
    print(", ".join(fichiers_sans_extension) if fichiers_sans_extension else "Aucun fichier sans extension trouvé.")

if __name__ == "__main__":
    main()

