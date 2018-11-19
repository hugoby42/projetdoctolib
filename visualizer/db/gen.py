import json
import random as rd


#On formalise l'ecriture des noms et prenoms
def formalise_nom(nom):
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

#On génère un nom et un prenom de façon random
nom=liste_noms[rd.randint(0,len(liste_noms)-1)]
prenom=liste_prenoms[rd.randint(0,len(liste_prenoms)-1)]

