#LIBRAIRIES
import json
import random as rd
import numpy as np
import visualizer.db.candidats.gen_random_date as grd
import visualizer.db.candidats.gen_random_identity as gri


#LISTES
liste_noms = gri.create_liste_noms()
liste_prenoms = gri.create_liste_prenoms()
liste_villes = gri.create_liste_villes()
liste_lieu_rdv = ['Eiffel','Bouygues','Breguet']
liste_etats = ['Postulé','Exercice donné','Code en cours de vérification','Fin de candidature','Refus','Recruté']



#On génère un candidat de façon random
def creation_candidat(id_candidat):
    nom = liste_noms[rd.randint(0,len(liste_noms)-1)]
    prenom = liste_prenoms[rd.randint(0,len(liste_prenoms)-1)]
    dateNaissance,dateEntretien = grd.dates_aleatoires_naissance_entretien()
    lieuNaissance = liste_villes[rd.randint(0,len(liste_villes)-1)]
    lieuEntretien = liste_lieu_rdv[rd.randint(0,len(liste_lieu_rdv)-1)]
    fichiers = gri.combien_fichier(id_candidat,dateEntretien)
    level = rd.randint(1,5)
    etat = rd.choice(liste_etats)
    return ({'id':id_candidat,'nom':nom,'prenom':prenom,'dateNaissance':dateNaissance,
            'lieuNaissance':lieuNaissance,'dateEntretien':dateEntretien,'lieuEntretien':lieuEntretien,
            'fichiers':fichiers,'etat':etat,'metrics':{'level':level}})


#On génère nb_candidats candidats
def creation_n_candidats(nombre_candidats):
    candidats = []
    for id_candidat in range(nombre_candidats):
        candidats.append(creation_candidat(id_candidat))
    return candidats
#print(creation_n_candidats(nombre_candidats))
