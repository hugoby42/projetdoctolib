import json

def getData(fileName="input.json"):
    inputFile = open(fileName)
    inputStr = inputFile.read()
    inputData = json.loads(inputStr)
    
    resultat = inputData["candidats"]

    return resultat



def queryData(data,selection):            #a faire: vérification des type #on part du principe qu'il n'y a qu'une seule 'selection' pour l'instatnt

# forme de la liste selection : [  [  [liste key, liste valeurs possibles] , [


    #fonction de selection
    def test(dict_candidate):           #problème : un seul truc possible, donc si on doit faire plusieurs selection, il faudra faire plusieurs test ^^

        for critere in selection:

            #on implemente les keys et les values qui sont attendues
            key=critere[0]
            list_values=critere[1]

            #on projete la valeur du dictionnaire du candidat qui nous interesse
            dict=dict_candidate
            nb_level=len(key)
            for i in range(nb_level-1):
                sous_liste=dict[key[i]]
                dict=sous_liste[0]      #dict doit être un dictionnaire

            #on vérifie que la clé est bien vérifiée
            if dict[key[nb_level-1]] not in list_values:
                return False

        return True


    selection_candidates=filter(test,data)

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


"""
#test

selection=[[['id'],[1]],[['fichiers','id'],[1]]]
data=getData()
list_candidat, list_values =queryData(data,selection)
"""




