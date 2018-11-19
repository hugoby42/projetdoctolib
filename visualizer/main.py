
from app import *

# Fonction principale assurant les différentes étapes du lancement de l'application

data = gen.main(100) # On crée une base de données de candidats aléatoire
db.access.update(data) # On enregistre cette base de données dans un fichier JSON
db.access.prettyPrint() # On affiche une partie de cette base de données dans le terminal
app.main.launch() # On lance l'application
