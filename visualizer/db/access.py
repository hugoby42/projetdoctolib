import json

def getData(fileName="input.json"):
    inputFile = open(fileName)
    inputStr = inputFile.read()
    inputData = json.loads(inputStr)
    
    resultat = inputData["candidats"]

    return resultat

print(getData())
