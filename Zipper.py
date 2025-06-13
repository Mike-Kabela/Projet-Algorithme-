import os
import zipfile

def zipper_par_extension(dossier_source):
    print("\n Création des archives ZIP...")

    for dossier in os.listdir(dossier_source):
        chemin_dossier = os.path.join(dossier_source, dossier)
        if os.path.isdir(chemin_dossier):
            zip_path = os.path.join(dossier_source, f"{dossier}.zip")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for racine, _, fichiers in os.walk(chemin_dossier):
                    for fichier in fichiers:
                        chemin_fichier = os.path.join(racine, fichier)
                        arcname = os.path.relpath(chemin_fichier, start=dossier_source)
                        zipf.write(chemin_fichier, arcname)
            print(f" {zip_path} créé.")
