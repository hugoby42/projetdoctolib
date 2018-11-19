Je suis sur sur ma branche Clara

Projet 2
meilleur format de données en entrée: json
Dossier qui comprend toutes les données: nom, prénom, date de naissance, formation, résultats des tests,
                                         nombre de fonctions utilisées, nombre de tests


Modèle de json:
 {
 “id”: ,
 “nom”: ,
 “prenom”: ,
 “dateNaissance”: ,
 “lieuNaissance”: ,
 “dateEntretien”: ,
 “lieuEntretien”: ,
 “fichiers”:
 [
   {
     “id” : ,
     “nom”: ,
     “contenu”: ,
     “nomTest”:,
     “contenu_Test”: ,
     “stats”:
     {
       “functionsCount”: ,
       “commentCount”: ,
       “variableNameQuality”: ,
       “duplicate”:
       [
         {
           “id”: ,
           “similarity”: ,
         }
       ]
     }
     “compteRendu”: ,
     “dateUpload”: ,
   }
 ],
 “metrics”:
 {
   “level”:
 }
}


Dash : crée des pages net sur notre pc
       récupère les données d'un tableau, mais pas d'un python


Plan de travail:
- création d'une DB de candidats automatiquement pour tester notre code
- création d'une bibliothèque Json qui permette de lire et de modifier les données
- passage sur DASH
