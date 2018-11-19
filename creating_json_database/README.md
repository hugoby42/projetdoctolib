#FORMAT DU FICHIER JSON
{
 “id”: int, #de 0 à 25
 “nom”: string,
 “prenom”: string,
 “dateNaissance”: datetime,
 “lieuNaissance”: string,
 “dateEntretien”: datetime,
 “lieuEntretien”: string,
 “fichiers”:
 [
   {
     “id” : ind, #id_candidat + num_fichier exemple candidat 1 premier fichier 1001
     “nom”: string,
     “contenu”: string,
     “nomTest”: string,
     “contenu_Test”: string,
     “stats”:
     {
       “functionsCount”: int,
       “commentCount”: int,
       “variableNameQuality”: float, #entre 0 et 1
       “duplicate”:
       [
         {
           “id”: int,
           “similarity”: string,
         }
       ]
     }
     “compteRendu”: string,
     “dateUpload”: datetime,
   }
 ],
 “metrics”:
 {
   “level”:int #1 à 5 1 c'est bien 5 c'est mauvais
 }
}
