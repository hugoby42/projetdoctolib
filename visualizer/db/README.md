DESCIPTION DU RETOUR DE GEN.PY
{
 “candidats”:
 [
 {
   “id”: int,#commence à 0 jusqu'à nombre_candidats
   “nom”: string,
   “prenom”: string,
   “dateNaissance”: string,jour/mois/année
   “lieuNaissance”: string,
   “dateEntretien”: string,jour/mois/année
   “lieuEntretien”: string,
   “fichiers”:
   [
     {
       “id” : string, ex: id_candidat =1 id='1001' pour le deuxième fichier uploadé, '1000' pour le premier
       “nom”: string,
       “contenu”: string,
       “nomTest”: string,
       “contenu_Test”: string,
       “stats”:
       {
         “functionsCount”: int, entre 0 et 100
         “commentCount”: int, entre 0 et 100
         “variableNameQuality”: float, entre 0 et 1
         “duplicate”:
         [
           {
             “id”: int, #identifiant du candidat sur lequel il a copié
             “similarity”: string
           }
         ]
       },
       “compteRendu”: string,
       “dateUpload”: string jour/mois/année
     }
   ],
   “etat”:string,
   “metrics”:
   {
     “level”: int #entre 1 et 5
   }
 }
 ]
}

