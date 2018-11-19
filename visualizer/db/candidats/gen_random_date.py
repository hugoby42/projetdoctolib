import time
import random

"""on écrit un programe qui crée des dates aléatoires entre la date start et la date end
1970 correspond à l'origine des temps (on ne peut pas atteindre des dates avant"""

def date_aleatoire_entre_start_end(start_date, end_date):
    '''crée une date aléatoire entre les dates start et end (1970 étant l'origine des temps, on ne peut pas
    atteindre les dates antérieures)
    :param start_date : str représentant la date de début
    :param end_date : str représentant la date de fin
    :return date : str représentant la date inventée
    '''
    format = '%d/%m/%Y %I:%M %p'
    nb = random.random()
    start_date = time.mktime(time.strptime(start_date, format))
    end_date = time.mktime(time.strptime(end_date, format))
    date = start_date + nb * (end_date - start_date)
    return time.strftime(format, time.localtime(date))


#print(date_aleatoire_entre_start_end("01/01/1970 01:30 PM", "31/12/1998 11:59 PM"))
#print(type(randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random())))

"""PROBLEME: l'origine des temps est située au 01/01/1970.
Pour atteindre des dates inférieures, il faut ruser (sinon "mktime argument out of range")
1970 correspond à l'origine des temps"""



"""on écrit un programe qui crée une date de naissance (entre 1970 et 1998) et une date d'entretien
(au mois de septembre 2018) aléatoires"""

def dates_aleatoires_naissance_entretien():
    '''retourne deux dates crées aléatoirement corresondant à la date de naissance et à la date d'entretien
    :return [dateNaissance, dateEntretien] : liste de str contenant la date de naissance (comprise entre 1970 et 1998) et la date d'entretien (mois de septembre 2018)'''
    dateNaissance = date_aleatoire_entre_start_end("01/01/1970 01:30 PM", "31/12/1998 11:59 PM")[:10]
    jour_entretien = random.randint(0,30)
    dateEntretien = str(jour_entretien) + "/09/2018"
    return [dateNaissance, dateEntretien]

print(type(dates_aleatoires_naissance_entretien()))

"""on crée une fonction qui crée aléatoirement une date de dépôt de fichiers, comprise dans les 5 jours
suivant la date de l'entretien"""

def date_depot_fichier(date_entretien):
    '''retourne une date de dépôt choisie aléatoirement dans les 5 jours suivant l'entretien
    :param date_entretien : str représentant la date d'entretien choisie aléatoirement
    :return date_depot : str représentant la date de dépôt'''
    jour_entretien_str = ''
    i = 0
    while date_entretien[i] != "/" :
        jour_entretien_str += date_entretien[i]
        i += 1
    jour_entretien = int(jour_entretien_str)
    jour_depot = random.randint(0,5)
    if jour_entretien+jour_depot <= 30:
        date_depot = str(jour_entretien+jour_depot) + "/09/2018"
    else:
        date_depot = str((jour_entretien+jour_depot)%30) + "/10/2018"
    return date_depot

#date_entretien = "29/09/2018"
#print(type(date_depot_fichier(date_entretien)))
