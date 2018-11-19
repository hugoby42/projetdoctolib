#LIBRARIES
import json
import random as rd
import numpy as np
import visualizer.db.get_random_date as grd


#On créer des candidats
nombre_candidats=2


#On formalise l'ecriture des noms et prenoms
def formalise_nom(nom):
    """ Retourne un nom (string) avec la premiere lettre en majuscule
    :param nom: nom propre
    :return: (str) un nom normalisé
    """
    nom=str(nom)
    nom=nom.replace(' ','')
    maj=nom[0].upper()
    min=nom[1:].lower()
    return(maj+min)

#On récupère des prénoms
prenoms=open("prenoms.txt",'r').readlines()

liste_prenoms=[]
for ligne in prenoms:
    ligne=ligne.replace('\n','')#on enlève les retours à la ligne
    lin=[]
    mot=''
    for car in ligne:
        if car =="\t":
            lin.append(mot)
            mot=''
        else:
            mot+=car
    lin.append(mot)
    if float(lin[3])>0 and '�' not in lin[0]: #la freqence du nom est non nulle et que � n'est pas dans le nom
        liste_prenoms.append(formalise_nom(lin[0]))#on ajoute un prénom à la liste des prénoms



#On récupère des noms
noms=open("noms.txt",'r').readlines()
liste_noms=[]
for ligne in noms:
    car=0
    while ligne[car] != '\t':
        car+=1
    liste_noms.append(formalise_nom(ligne[:car]))



#On rècupère une liste de villes
villes=open("villes_france.csv", "r").readlines()
liste_villes=[]
for ville in villes:
    rang_premiere_virgule=0
    while ville[rang_premiere_virgule]!=',':
        rang_premiere_virgule+=1
    rang_min=rang_premiere_virgule+1
    while ville[rang_min]!=',':
        rang_min+=1
    rang_max=rang_min+1
    while ville[rang_max]!=',':
        rang_max+=1
    ville=ville[rang_min+1:rang_max]
    ville=ville[1:-1]#On enlève les doubles guillemets
    liste_villes.append(formalise_nom(ville))

#Liste de lieux de RDV
liste_lieu_rdv=['Eiffel','Bouygues','Breguet']


##############On créer des fichiers avec des stats
nom_fichier_python="exercise.py"
contenu_python="""
def sum(a,b):
    return(a+b)"""
nom_fichier_test_python="test_exercise.py"
contenu_test="""
import pytest
import exercise.py as Ex

def test_sum():
    assert ( Ex.sum(a,b)== a+b)"""

def combien_fichier(id_candidat,dateEntretien,nombre_candidats):
    """ Retourne une liste de dictionnaires représentant les fichiers envoyés par le candidat
    :param id_candidat: entier représentant un candidat
    :param dateEntretien: str représentant la date de l'entretien (JJ/MM/AAAA)
    :param nombre_candidats: entier représentant le nombre de candidats au total
    :return: (list) une liste de fichier envoyé par le candidats
    """
    nombre_fichiers=int((np.random.exponential(9,1))//1)
    fichiers=[]
    for num_fichier in range(nombre_fichiers):
        id=str(id_candidat)+str(num_fichier//100)+str(num_fichier//10)+str(num_fichier//1)
        nom=nom_fichier_python
        contenu=contenu_python
        nomTest=nom_fichier_test_python
        contenu_Test=contenu_test
        dateUpload=grd.date_depot_fichier(dateEntretien)
        stats={"functionsCount": rd.randint(0,100),"commentCount": rd.randint(0,100),
                "variableNameQuality": rd.random(),"duplicate": As_tu_copier(id_candidat,nombre_candidats),
                "compteRendu":"Bon code!",'dateUpload' :dateUpload}
        fichiers.append({'id':id,'nom':nom,'contenu':contenu,'nomTest':nomTest,'contenu_Test':contenu_Test,'stats':stats})
    return(fichiers)

#CHEATING
def As_tu_copier(id_candidat,nombre_candidats):
    """ Retourne une liste de dictionnaires représentant les simillarits avec les autres codes
    :param id_candidat: entier représentant un candidat
    :param nombre_candidats: entier représentant le nombre de candidats au total
    :return: (list) une liste de simillarités avec les autres candidats
    """
    if nombre_candidats==1:
        return []
    else:
        nombre_similarity=int((np.random.exponential(9,1))//1)#nombre de triches
        similarities=[]
        for cheat in range(nombre_similarity):
            id_candidat_triche=rd.randint(0,nombre_candidats-2)
            if id_candidat_triche>=id_candidat:
                id_candidat_triche+=1
            contenu_triche="a+b"
            similarities.append({'id':id_candidat_triche,'similarity':contenu_triche})
        return(similarities)

#Etat de la candidature
etats=['Postulé','Exercice donné','Code en cours de vérification','Fin de candidature','Refus','Recruté']


#On génère un candidat de façon random
def creation_candidat(id_candidat,nombre_candidats):
    """ Retourne un dictionnaires représentant le candidat
    :param id_candidat: entier représentant un candidat
    :param nombre_candidats: entier représentant le nombre de candidats au total
    :return: (dict) un dictionnaire représentant le candidat
    """
    nom=liste_noms[rd.randint(0,len(liste_noms)-1)]
    prenom=liste_prenoms[rd.randint(0,len(liste_prenoms)-1)]
    dateNaissance,dateEntretien=grd.dates_aleatoires_naissance_entretien()
    lieuNaissance=liste_villes[rd.randint(0,len(liste_villes)-1)]
    lieuEntretien=liste_lieu_rdv[rd.randint(0,len(liste_lieu_rdv)-1)]
    fichiers=combien_fichier(id_candidat,dateEntretien,nombre_candidats)
    level=rd.randint(1,5)
    etat=rd.choice(etats)
    return ({'id':id_candidat,'nom':nom,'prenom':prenom,'dateNaissance':dateNaissance,
            'lieuNaissance':lieuNaissance,'dateEntretien':dateEntretien,'lieuEntretien':lieuEntretien,
            'fichiers':fichiers,'etat':etat,'metrics':{'level':level}})

def creation_n_candidats(nombre_candidats):
    """ Retourne une liste de dictionnaires représentant tous les candidats de la base de données
    :param nombre_candidats: entier représentant le nombre de candidats au total
    :return: (list) une liste de dictionnaires pour représenter chaque candidat
    """
    candidats=[]
    for id_candidat in range(nombre_candidats):
        candidats.append(creation_candidat(id_candidat,nombre_candidats))
    return candidats
print(creation_n_candidats(nombre_candidats))
