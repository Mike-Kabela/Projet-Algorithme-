import datetime
import csv
#structure de données pour stocker les logs
journal = []
def ajouter__entree(action, fichier,destination=None,erreur=None):
    ""
    #Ajoute une entrée au journal des opérations.
    ""
    entree={
        "timestamp":
    datetime.datetime.now().isoformat(sep='',timespec='seconds'),
     "action": action,
     "fichier":fichier,
     "destination":destination,
     "erreur":erreur,
  }
    journal.append(entree)
    def afficher_journal():
        ""
        #affiche le journal des operations.
        if not journal:
            print("journal vide")
            return
        print("\njournal des opérations")
        for log in journal:
            print(f"[{log ['timestamp'] }]{log['action'].upper()}-{log['fichier']}",end="")
            if log["destination"]:
                print(f"-> {log['destination']}",end="")                  
            if log ["erreur"]:
              print(f"! erreur:{entree['erreur']}",end="")
print()
def Exporter_journal_csv(nom_fichier="journal_operation.csv"):
    ""
    if not journal:
        print("Aucun log à exporter.")
        return
    try:
        with open(nom_fichier,mode="w",newline='',encoding="utf-8") as fichier:
            writer=csv.DictWriter(fichier,fieldnames=["timestamp",
                            "action","fichier","destination","erreur"])
            writer.writeheader()
            for log in journal:
                writer.writerow(log)
        print(f" le journal a été exporte avec succés dans le fichier:{nom_fichier}")
    except Exception as e:
        print(f"erreur lors de l'exportation du journal :{e}")
