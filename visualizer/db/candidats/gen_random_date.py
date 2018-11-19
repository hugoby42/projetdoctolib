import time
import random

"""on écrit un programe qui crée des dates de naissance aléatoires entre 1970 et 1998
1970 correspond à l'origine des temps"""


def date_aleatoire_entre_start_end(start_date, end_date):
    format = '%d/%m/%Y %I:%M %p'
    nb = random.random()
        #on passe les chaînes de caractères en datetime
        #il faut qu'elles soient données dans le format spécifié
    start_date = time.mktime(time.strptime(start_date, format))
    end_date = time.mktime(time.strptime(end_date, format))
        #on calcule la nouvelle date
    date = start_date + nb * (end_date - start_date)
        #on la transforme en string
    return time.strftime(format, time.localtime(date))


#print(date_aleatoire_entre_start_end("01/01/1970 01:30 PM", "31/12/1998 11:59 PM"))
#print(type(randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random())))

"""PROBLEME: l'origine des temps est située au 01/01/1970.
Pour atteindre des dates inférieures, il faut ruser (sinon "mktime argument out of range")
1970 correspond à l'origine des temps"""


"""on écrit un programe qui crée une date de naissance (entre 1970 et 1998), 
une date d'entretien (au mois de septembre 2018) et une date de dépôt de l'exercice (dans les 5 jours 
qui suivent l'entretien) aléatoires"""

def dates_aleatoires():
    dateNaissance = date_aleatoire_entre_start_end("01/01/1970 01:30 PM", "31/12/1998 11:59 PM")[:10]
    jour_entretien = random.randint(0,30)
    dateEntretien = str(jour_entretien) + "/09/2018"
    jour_depot = random.randint(0,5)
    if jour_entretien+jour_depot <= 30:
        dateDepot = str(jour_entretien+jour_depot) + "/09/2018"
    else:
        dateDepot = str(jour_entretien+jour_depot % 30) + "/10/2018"
    return [dateNaissance, dateEntretien, dateDepot]



print (dates_aleatoires())
