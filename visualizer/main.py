import visualizer.db.gen as gen
import visualizer.db.access as access
import visualizer.app.main as app_main


# Fonction principale assurant les différentes étapes du lancement de l'application

data = gen.main(100) # On crée une base de données de candidats aléatoire
access.update(data) # On enregistre cette base de données dans un fichier JSON
access.prettyPrint() # On affiche une partie de cette base de données dans le terminal
app_main.launch() # On lance l'application
