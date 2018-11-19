import json
import os



def getData(fileName = "input.json"):
    # Fonction ouvrant le fichier JSON contenant la liste 
    # des candidats et renvoyant une liste de dictionnaires, 
    # chacun contenant les informations relatives à un candidat
    with open(fileName, "r+") as inputFile:
        inputStr = inputFile.read()
        inputData = json.loads(inputStr)
    
        data = inputData["candidats"]

        inputFile.close()

        return data



def prettyPrint(fileName = "input.json"):
    # Fonction affichant humainement le fichier JSON dans le terminal
    data = getData(fileName)

    print(json.dumps(data, indent=4, sort_keys=False))



def update(data = [], fileName = "input.json"):
    # Après de multiples modifications sur la variable data 
    # contenant l'équivalent du fichier JSON, cette fonction 
    # met à jour les modifications en les enregistrant dans le fichier JSON en question
    os.remove(fileName)

    with open(fileName, "w") as inputFile: 
        json.dump(data, inputFile, indent=4)
        inputFile.close()
