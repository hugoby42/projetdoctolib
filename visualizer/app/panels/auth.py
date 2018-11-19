import getpass as gp
import base64
import os

#from passlib.hash import pbkdf2_sha256 # deuxième méthode pour encrypter le mot de passe
from passlib.context import CryptContext

pwdContext = CryptContext(schemes=["sha512_crypt"],
                           default="sha512_crypt",
                           sha512_crypt__default_rounds=45000)



def toHash(s):
    # Fonction dérivant le hash associé à une chaîne de caractères
    hash = pwdContext.hash(s)
    return hash

def storeHash(login, password):
    # Fonction enregistrant le hash associé au couple login / mot de passe dans le fichier auth.hash
    with open("auth.hash", "w") as fichierHash:
        fichierHash.write(toHash(login))
        fichierHash.write("\n")
        fichierHash.write(toHash(password))

        fichierHash.close()
        print("Couple login / password correctement enregistré.")



def getHash(login, password):
    # Fonction récupérant le hash associé au couple login / mot de passe stocké dans le fichier auth.hash
    with open("auth.hash", "r") as fichierHash:
        store = fichierHash.readlines()
        hashLogin, hashPassword = store[0].strip(), store[1].strip() # On se débarasse des caractères superflus
        print(hashLogin, hashPassword)

        fichierHash.close()
        return hashLogin, hashPassword



def verify(login, password):
    hashLogin, hashPassword = getHash(login, password)

    return (pwdContext.verify(login, hashLogin), pwdContext.verify(password, hashPassword))



def setHash():
    login = input("Veuillez entrer le login : ").strip()
    password = gp.getpass("Veuillez entrer le mot de passe : ").strip()
    
    storeHash(login, password)



def setAuth(regen=False):
    # Si la clé hash n'existe pas ou si le fichier qui la contient ne semble pas contenir de clé hash, demander à l'utilisateur de la créer
    # Si regen, alors le programme demande malgré tout à l'utilisateur d'entrer un nouveau couple login / password
    if regen:
        setHash()
    if not os.path.isfile("auth.hash"):
        print("Couple login / password introuvable. Veuillez le réinitialiser.")
        setHash()
    elif os.stat("auth.hash").st_size <= 10:
        print("Couple login / password endommagé. Veuillez le réinitialiser.")
        setHash()



setAuth()
