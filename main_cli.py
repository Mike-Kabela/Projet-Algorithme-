from directory_scanner import demander_chemin_dossier, lister_fichiers, detecter_extensions
from file_organizer import creer_dossier_destination, deplacer_fichier

def main():
    print("CLASSIFICATEUR DE FICHIERS PAR EXTENSION\n")

    # Étape 1 : Obtenir le dossier source
    dossier_source = demander_chemin_dossier()

    # Étape 2 : Lister les fichiers
    fichiers = lister_fichiers(dossier_source)
    if not fichiers:
        print("Aucun fichier trouvé dans ce dossier.")
        return

    print(f" {len(fichiers)} fichier(s) trouvé(s). Analyse en cours...\n")

    # Étape 3 : Séparer les fichiers avec et sans extension
    fichiers_par_extension, fichiers_sans_extension = detecter_extensions(fichiers)

    # Étape 4 : Organiser les fichiers par extension
    for extension, fichiers in fichiers_par_extension.items():
        dossier_cible = creer_dossier_destination(dossier_source, extension)
        for fichier in fichiers:
            nouvelle_destination = deplacer_fichier(fichier, dossier_cible)
            print(f" {fichier} → {nouvelle_destination}")

    # Étape 5 : Gérer les fichiers sans extension
    if fichiers_sans_extension:
        dossier_sans_ext = creer_dossier_destination(dossier_source, "SANS_EXTENSION")
        for fichier in fichiers_sans_extension:
            nouvelle_destination = deplacer_fichier(fichier, dossier_sans_ext)
            print(f" (Sans extension) {fichier} → {nouvelle_destination}")

    # Résumé final
    print("\n Classement terminé.")
    print(f"Total fichiers traités : {len(fichiers)}")
    print(f"Extensions détectées : {', '.join(fichiers_par_extension.keys()).upper()}")
    print(f"Fichiers sans extension : {len(fichiers_sans_extension)}")

if __name__ == "__main__":
    main()




