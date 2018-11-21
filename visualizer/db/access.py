import json
import os

# index :
# 1. getData
# 2. prettyPrint
# 3. update
# 4. query



def getData(fileName = "db/input.json"):
    # Fonction ouvrant le fichier JSON contenant la liste 
    # des candidats et renvoyant une liste de dictionnaires, 
    # chacun contenant les informations relatives à un candidat
    with open(fileName, "r+") as inputFile:
        inputStr = inputFile.read()
        inputData = json.loads(inputStr)

        inputFile.close()

        return inputData



def prettyPrint(fileName = "db/input.json"):
    # Fonction affichant humainement le fichier JSON dans le terminal
    data = getData(fileName)
    candidats = json.dumps(data, indent=4, sort_keys=False)
    
    print("Voici l'ensemble des candidats en lice :\n\n\n")
    print(candidats)



def update(data = [], fileName = "db/input.json"):
    # Après de multiples modifications sur la variable data 
    # contenant l'équivalent du fichier JSON, cette fonction 
    # met à jour les modifications en les enregistrant dans le fichier JSON en question
    os.remove(fileName)

    with open(fileName, "w") as inputFile: 
        json.dump(data, inputFile, indent=4)
        inputFile.close()



def query(data,selection):

# forme de la liste selection : [  [  [liste key, liste valeurs possibles] , [


    #fonction de selection
    def test(dict_candidate):

        for critere in selection:

            #on implemente les keys et les values qui sont attendues
            key=critere[0]
            list_values=critere[1]

            #on projete la valeur du dictionnaire du candidat qui nous interesse

            dict=dict_candidate
            nb_level=len(key)
            for i in range(nb_level-1):
                sous_liste=dict[key[i]]
                if sous_liste==[]:
                    return False
                dict=sous_liste[0]      #dict doit être un dictionnaire

            #on vérifie que la clé est bien dans les valeurs demandées
            if dict[key[nb_level-1]] not in list_values:
                return False

        return True


    selection_candidates=list(filter(test,data))

    #liste ds values qui nous interessent
    list_values=[]
    for candidat in selection_candidates:

        list_temp=[]

        for critere in selection:

            #on implemente les keys et les values qui sont attendues
            key=critere[0]
            list_values=critere[1]

            #on projete la valeur du dictionnaire du candidat qui nous interesse
            dict=candidat
            nb_level=len(key)
            for i in range(nb_level-1):
                sous_liste=dict[key[i]]
                dict=sous_liste[0]      #dict doit être un dictionnaire

            #on ajoute la velur cherchée à la liste des values
            list_temp.append(dict[key[nb_level-1]])

        list_values.append(list_temp)

    return selection_candidates, list_values


"""selection=[[['id'],[1]],[['fichiers','id'],[1]]]
data = getData()
list_candidat, list_values = query(data,selection)"""
