
import os
import shutil

def reinitialiser_dossier(dossier_source):
    print("\n Réinitialisation en cours...")

    for dossier in os.listdir(dossier_source):
        chemin_dossier = os.path.join(dossier_source, dossier)
        if os.path.isdir(chemin_dossier):
            for fichier in os.listdir(chemin_dossier):
                chemin_fichier = os.path.join(chemin_dossier, fichier)
                nouveau_chemin = os.path.join(dossier_source, fichier)

                base, ext = os.path.splitext(fichier)
                compteur = 1
                while os.path.exists(nouveau_chemin):
                    nouveau_chemin = os.path.join(dossier_source, f"{base}({compteur}){ext}")
                    compteur += 1

                shutil.move(chemin_fichier, nouveau_chemin)
            shutil.rmtree(chemin_dossier)

    print("Réinitialisation terminée.")
