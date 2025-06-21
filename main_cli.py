# Importation des fonctions depuis les autres modules du projet
from directory_scanner import scanner_dossier                      # Pour scanner le dossier source
from file_organizer import organiser_fichiers                      # Pour classer les fichiers
from logger import afficher_journal, exporter_journal_csv          # Pour afficher/exporter le journal
from stats_reporter import afficher_statistiques, exporter_stats_csv  # Pour les statistiques
from zipper import zipper_par_extension                            # Fonction bonus : créer ZIP par extension
from searcher import rechercher_fichiers                           # Fonction bonus : rechercher un fichier par nom
from resetter import reinitialiser_dossier                         # Fonction bonus : remettre les fichiers à la racine

# Initialisation des structures utilisées dans tout le programme
fichiers_par_extension = {}          # Dictionnaire : {".pdf": [fichier1, fichier2], ...}
fichiers_sans_extension = []         # Liste des fichiers sans extension
journal = []                         # Liste des opérations effectuées (journal)
dossier_source = ""                  # Chemin du dossier choisi par l’utilisateur

# Définition de la fonction principale du menu CLI
def menu():
    global dossier_source  # Pour modifier la variable globale dans la fonction

    while True:  # Boucle infinie pour maintenir le menu actif
        # Affichage du menu principal
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Trier les fichiers")
        print("2 - Afficher les statistiques")
        print("3 - Afficher le journal des opérations")
        print("4 - Quitter")
        print("5 - Créer des archives ZIP")
        print("6 - Rechercher un fichier par nom")
        print("7 - Réinitialiser (tout remettre à la racine)")

        # Demande de choix à l’utilisateur
        choix = input("Votre choix : ")

        # === Option 1 : Trier les fichiers ===
        if choix == "1":
            # L'utilisateur fournit le dossier à classer
            dossier_source, fichiers_par_extension, fichiers_sans_extension = scanner_dossier()
            # On organise les fichiers dans les sous-dossiers correspondants
            organiser_fichiers(dossier_source, fichiers_par_extension, fichiers_sans_extension, journal)

        # === Option 2 : Afficher les statistiques ===
        elif choix == "2":
            # On affiche les stats dans la console
            afficher_statistiques(dossier_source, fichiers_par_extension, fichiers_sans_extension)
            # Et on les exporte au format CSV
            exporter_stats_csv(dossier_source, fichiers_par_extension, fichiers_sans_extension)

        # === Option 3 : Afficher le journal des opérations ===
        elif choix == "3":
            # Affiche le journal en console
            afficher_journal(journal)
            # Exporte le journal dans un fichier CSV
            exporter_journal_csv(dossier_source, journal)

        # === Option 4 : Quitter le programme ===
        elif choix == "4":
            print("Au revoir !")
            break  # Sortie de la boucle → arrêt du programme

        # === Option 5 : Créer des fichiers ZIP ===
        elif choix == "5":
            if dossier_source:
                zipper_par_extension(dossier_source)  # Création des archives par type
            else:
                print("Vous devez d'abord trier les fichiers.")

        # === Option 6 : Rechercher un fichier par nom ===
        elif choix == "6":
            if dossier_source:
                mot = input("Entrez le mot-clé à chercher : ")  # Demande le nom à rechercher
                rechercher_fichiers(dossier_source, mot)
            else:
                print("Classez les fichiers avant de chercher.")

        # === Option 7 : Réinitialiser le classement ===
        elif choix == "7":
            if dossier_source:
                confirm = input("Confirmer la réinitialisation ? (o/n) : ")
                if confirm.lower() == "o":
                    reinitialiser_dossier(dossier_source)  # Supprime les dossiers et remet tous les fichiers à la racine
                    fichiers_par_extension.clear()         # Réinitialisation des structures de suivi
                    fichiers_sans_extension.clear()
            else:
                print("Vous devez d'abord trier les fichiers.")

        # === Cas d'erreur : option invalide ===
        else:
            print("Option invalide.")

# Point d’entrée du programme
if __name__ == "__main__":
    menu()  # Lance le menu si ce fichier est exécuté directement




