import json
import random as rd
import numpy as np

#On créer des candidats
nombre_candidats=40
#On formalise l'ecriture des noms et prenoms
def formalise_nom(nom):
    nom=nom.replace(' ','')
    nom=str(nom)
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


#On créer des fichiers avec des stats
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
functionsCount=rd.randint(0,100)
commentCount=rd.randint(0,100)
variableNameQuality=rd.random()
compteRendu="Bon code!"
level=rd.randint(1,5)
def As_tu_copier():
    nombre_similarity=int((np.random.exponential(9,1))//1)#nombre de triches
    similarities=[]
    for cheat in range(nombre_similarity):
        id_candidat=rd.randint(0,nombre_candidats-1)
        contenu_triche="a+b"
        similarities.append({'id':id_candidat,'similarity':contenu_triche})
    return(similarities)
print(As_tu_copier())

#On génère un candidat de façon random
nom=liste_noms[rd.randint(0,len(liste_noms)-1)]
prenom=liste_prenoms[rd.randint(0,len(liste_prenoms)-1)]
ville_de_naissance=liste_villes[rd.randint(0,len(liste_villes)-1)]
lieu_rdv=liste_lieu_rdv[rd.randint(0,len(liste_lieu_rdv)-1)]
