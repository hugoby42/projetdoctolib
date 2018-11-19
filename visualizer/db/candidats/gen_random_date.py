import time
import random

"""on écrit un programe qui crée des dates aléatoires entre la date start et la date end
1970 correspond à l'origine des temps (on ne peut pas atteindre des dates avant"""

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



"""on écrit un programe qui crée une date de naissance (entre 1970 et 1998) et une date d'entretien
(au mois de septembre 2018) aléatoires"""

def dates_aleatoires_naissance_entretien():
    dateNaissance = date_aleatoire_entre_start_end("01/01/1970 01:30 PM", "31/12/1998 11:59 PM")[:10]
        #on récupère seulement la date
    jour_entretien = random.randint(0,30)
    dateEntretien = str(jour_entretien) + "/09/2018"
    return [dateNaissance, dateEntretien]

#print(dates_aleatoires_naissance_entretien())

"""on crée une fonction qui crée aléatoirement une date de dépôt de fichiers, comprise dans les 5 jours
suivant la date de l'entretien"""

def date_depot_fichier(date_entretien):
    jour_entretien = int(date_entretien[:2])
    jour_depot = random.randint(0,5)
    if jour_entretien+jour_depot <= 30:
        date_depot = str(jour_entretien+jour_depot) + "/09/2018"
    else:
        date_depot = str((jour_entretien+jour_depot)%30) + "/10/2018"
    return date_depot

#date_entretien = "29/09/2018"
#print(date_depot_fichier(date_entretien))
