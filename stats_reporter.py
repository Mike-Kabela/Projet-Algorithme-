import os
import csv

# Calcule le nombre total de fichiers et par extension
def calculer_statistiques(fichiers_par_extension, fichiers_sans_extension):
    total_fichiers = sum(len(lst) for lst in fichiers_par_extension.values()) + len(fichiers_sans_extension)
    stats_par_extension = {ext: len(lst) for ext, lst in fichiers_par_extension.items()}
    stats_par_extension["SANS_EXTENSION"] = len(fichiers_sans_extension)

    # Calcul des pourcentages
    stats_pourcentage = {}
    for ext, count in stats_par_extension.items():
        pourcentage = (count / total_fichiers) * 100 if total_fichiers > 0 else 0
        stats_pourcentage[ext] = round(pourcentage, 2)

    return total_fichiers, stats_par_extension, stats_pourcentage


# Affiche un rapport clair des stats
def afficher_rapport(total, par_ext, pourcentages):
    print("\n Rapport Statistiques :")
    print(f"Total fichiers traités : {total}\n")
    print("Nombre de fichiers par type :")
    for ext, count in par_ext.items():
        print(f" - {ext.upper()}: {count} ({pourcentages[ext]}%)")


# (Bonus) Affiche une arborescence simple des dossiers créés
def afficher_arborescence(dossier_racine):
    print("\n Arborescence des dossiers créés :")
    for racine, dossiers, fichiers in os.walk(dossier_racine):
        niveau = racine.replace(dossier_racine, "").count(os.sep)
        indent = " " * 4 * niveau
        print(f"{indent}- {os.path.basename(racine)}")
        for fichier in fichiers:
            print(f"{indent}    {fichier}")


# (Bonus) Export CSV des stats
def exporter_stats_csv(chemin_fichier, par_ext):
    try:
        with open(chemin_fichier, mode="w", newline="", encoding="utf-8") as fichier_csv:
            writer = csv.writer(fichier_csv)
            writer.writerow(["Extension", "Nombre de fichiers"])
            for ext, count in par_ext.items():
                writer.writerow([ext, count])
        print(f"Statistiques exportées vers {chemin_fichier}")
    except Exception as e:
        print(f"Erreur lors de l'export des statistiques : {e}")


