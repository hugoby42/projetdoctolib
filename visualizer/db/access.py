import json
import os

# index :
# 1. getData
# 2. prettyPrint
# 3. update
# 4. query
#Trouver fichier json
directory=os.getcwd()
if directory[len(directory)-10:]=='visualizer':
    os.chdir('./db')
elif directory[len(directory)-3:]=='app':
    os.chdir('../')
    os.chdir('.db')
elif directory[len(directory)-6:]=='panels':
    os.chdir('../../')
    os.chdir('./db')


def getData(fileName = "input.json"):
    # Fonction ouvrant le fichier JSON contenant la liste 
    # des candidats et renvoyant une liste de dictionnaires, 
    # chacun contenant les informations relatives à un candidat
    with open(fileName, "r+") as inputFile:
        inputStr = inputFile.read()
        inputData = json.loads(inputStr)

        inputFile.close()

        return inputData



def prettyPrint(fileName = "input.json"):
    # Fonction affichant humainement le fichier JSON dans le terminal
    data = getData(fileName)
    candidats = json.dumps(data, indent=4, sort_keys=False)
    
    print("Voici l'ensemble des candidats en lice :\n\n\n")
    print(candidats)



def update(data = [], fileName = "input.json"):
    # Après de multiples modifications sur la variable data 
    # contenant l'équivalent du fichier JSON, cette fonction 
    # met à jour les modifications en les enregistrant dans le fichier JSON en question
    os.remove(fileName)

    with open(fileName, "w") as inputFile: 
        json.dump(data, inputFile, indent=4)
        inputFile.close()



def query(data,list_queries):

#selection est une liste de sous-liste : chaque sous-liste correspond à un paramètre à selectionner [[keys],[values]] - si on veut tout selectionner, on met [key]['all']
#on fait un équivalent en SQL : selection=dictionaire

    #création de la liste qui va selc
    selection=[]
    for critere in list_queries:
        if critere[1][0]!='all':
            selection.append(critere)

    print(selection)

    #fonction de selection
    def test(dict_candidate):

        for critere in selection:

            #on implemente les keys et les values qui sont attendues
            list_keys=critere[0]      #key est une liste!
            list_values=critere[1]  #list

            #on projete la valeur du dictionnaire du candidat qui nous interesse
            dict=dict_candidate
            nb_level=len(list_keys)
            for i in range(nb_level-1):
                sous_liste=dict[list_keys[i]]
                if sous_liste==[]:
                    return False
                dict=sous_liste[0]      #dict doit être un dictionnaire

            #on vérifie que la clé est bien dans les valeurs demandées
            if dict[list_keys[nb_level-1]] not in list_values:
                return False

        return True


    candidates_selected=list(filter(test,data))         #on effectue la selection des candidats qui nous interessent

    #on récupère la liste des values qui nous interessent parmi les candidats selectionnés
    list_values_to_return=[]

    for candidat in candidates_selected:

        list_temp=[]

        for critere in list_queries:

            #on implemente les keys
            key=critere[0]

            #on projete la valeur du dictionnaire du candidat qui nous interesse
            dict=candidat
            nb_level=len(key)
            for i in range(nb_level-1):
                sous_liste=dict[key[i]]
                dict=sous_liste[0]      #dict doit être un dictionnaire

            #on ajoute la valeur cherchée à la liste des valeurs a renvoyer
            list_temp.append(dict[key[nb_level-1]])

        list_values_to_return.append(list_temp)

    return candidates_selected, list_values_to_return


"""

###Petite explication sur la list_queries qui est en entrée de query():
list_query=[sous-liste_1, sous-liste_2, ..]
sous-liste=[liste des clés, liste des valeurs que vous voulez obtenir pour les clés]
liste des clés : ex ['id'] ou ['fichiers','id']  (il faut prendre en comte les niveaux du dictionnaire
liste des valeurs : ['all']  si vous voulez tout selectionner, ['1','2','3'] si vous voulez selectionner uniquement les valeurs 1,2,3

Exemple : si vous voulez obtenir les nom, prénom des candidat dont l' 'id' de ficheir est compris entre 1 et 5, la list_queries est:
[[['prenom'],['all']],[['nom'],['all']],[['fichier','id'],['1','2','3','4','5']]]
"""
