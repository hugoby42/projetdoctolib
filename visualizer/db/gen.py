import json


"""on va créer une database qui va servir de test contenant toutes les infos sur les candidats
elle sera sous la forme d'un dossier json"""

def creer_database(n): #nombre de candidats dans la database
    database = {}
    for k in range (n):
        candidat = {}
        candidat["nom"] =
        candidat["prenom"] =
        candidat["dateNaissance"] =
        candidat["lieuNaissance"] =
        candidat["lieuEntretien"] =
        candidat["fichiers"] =
        candidat["metrics"] =


        database["candidat" = k] = candidat



def creer_liste_prenoms():







"""Modèle de json:
 {
 “id”: int de 1 à n,
 “nom”: str ,
 “prenom”: str,
 “dateNaissance”: datetime,
 “lieuNaissance”: str,
 “dateEntretien”: datetime,
 “lieuEntretien”: str,
 “fichiers”:
 [
   {
     “id” : int de la forme id_candidat + num_fichier (ex 1er candidat, 1er fichier: 1001) ,
     “nom”: str,
     “contenu”: str ,
     “nomTest”: str,
     “contenu_Test”: str,
     “stats”:
     {
       “functionsCount”: int ,
       “commentCount”: int,
       “variableNameQuality”: ,
       “duplicate”:
       [
         {
           “id”: ,
           “similarity”: ,
         }
       ]
     }
     “compteRendu”: str,
     “dateUpload”: ,
   }
 ],
 “metrics”:
 {
   “level”:
 }
}
"""
