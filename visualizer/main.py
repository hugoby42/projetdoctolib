from visualizer.app import *
import visualizer.app.main as app
import visualizer.db.gen as dbGen
import visualizer.db.access as dbAccess


# Fonction principale assurant les différentes étapes du lancement de l'application

data = dbGen.creation_n_candidats(100) # On crée une base de données de candidats aléatoire
dbAccess.update(data) # On enregistre cette base de données dans un fichier JSON
dbAccess.prettyPrint() # On affiche une partie de cette base de données dans le terminal
#app.main.launch() # On lance l'application
