import csv
import datetime

# Liste pour stocker les logs en mémoire
journal_operations = []

# Fonction pour ajouter une entrée au journal
def enregistrer_action(action, fichier_original, fichier_final, commentaire=""):
    entree = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,  # Exemple : "déplacé", "renommé", "erreur"
        "fichier_original": fichier_original,
        "fichier_final": fichier_final,
        "commentaire": commentaire
    }
    journal_operations.append(entree)

# Fonction pour afficher le journal à l'écran
def afficher_journal():
    print("\n Journal des opérations :")
    for ligne in journal_operations:
        print(f"[{ligne['date']}] {ligne['action']} : {ligne['fichier_original']} → {ligne['fichier_final']} ({ligne['commentaire']})")

# Bonus : Exporter le journal en CSV
def exporter_journal_csv(chemin_fichier):
    try:
        with open(chemin_fichier, mode='w', newline='', encoding='utf-8') as fichier_csv:
            champs = ["date", "action", "fichier_original", "fichier_final", "commentaire"]
            writer = csv.DictWriter(fichier_csv, fieldnames=champs)
            writer.writeheader()
            writer.writerows(journal_operations)
        print(f" Journal exporté avec succès vers {chemin_fichier}")
    except Exception as e:
        print(f"Erreur lors de l'export du journal : {e}")



