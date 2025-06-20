#calculer_et_afficher_toutes_les_statistiques_demandees

def calculer_statistiques(dossier):
    total_fichiers = 0
    types_fichiers = {}
    for racine, _, fichiers in os.walk(dossier):
        for fichier in fichiers:
            total_fichiers += 1
            ext = os.path.splitext(fichier)[1]
            types_fichiers[ext] = types_fichiers.get(ext, 0) + 1
    return total_fichiers,types_fichiers
#afficher_l_arborescence_des_dossiers_crees

def afficher_arborescence(dossier):
    for racine, dossiers, fichiers in os.walk(dossier):
        niveau = racine.replace(dossier, '').count(os.sep)
        indent = ' ' * 4 * niveau
        print(f"{indent}{os.path.basename(racine)}/")
        for f in fichiers:
            print(f"{indent}    {f}")
            
#preparation_des_donnees_pour_l_export_CVS

def exporter_statistiques_csv(stats, chemin_fichier):
    with open(chemin_fichier, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Extension', 'Nombre de fichiers'])
        for ext, count in stats.items():
            writer.writerow([ext,count])
            
#implemantation_de_la_creation_d_archives_ZIP

def creer_archive_zip(dossier_source, nom_archive):
    shutil.make_archive(nom_archive, 'zip',dossier_source)
