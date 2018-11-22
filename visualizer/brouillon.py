from datetime import datetime

def nb_jours_avant_depot(candidat):
    date_entretien = datetime.strptime(candidat['dateEntretien'], '%b/%d/%Y')
    nb_fichiers = len(candidat['fichiers'])
    nb_jours_avant_depot_moyen = 0
    for fichier in candidat["fichiers"]:
        date_depot = datetime.strptime(fichier['stats']['dateUpload'], '%b/%d/%Y')
        nb_jours_avant_depot_moyen += int((date_depot - date_entretien).days)
    return nb_jours_avant_depot_moyen/nb_fichiers

#print("23/06/1974"[6:])


"""code pour reremplir automatiquement input.json, à run dans main"""

from visualizer.app import *
#import visualizer.app.main as app
import visualizer.db.gen as dbGen
#import visualizer.db.access as dbAccess
from visualizer.db.access import update
# Fonction principale assurant les différentes étapes du lancement de l'application

data = dbGen.creation_n_candidats(100) # On crée une base de données de candidats aléatoire
print(data)
update(data)
print('ok')
#dbAccess.update(data) # On enregistre cette base de données dans un fichier JSON
#dbAccess.prettyPrint() # On affiche une partie de cette base de données dans le terminal
#app.main.launch() # On lance l'application
