from datetime import datetime


#fonction qui calcule le nb de jours moyen entre l'entretien et le dépôt pour un candidat

def nb_jours_avant_depot(candidat):
    date_entretien = datetime.strptime(candidat['dateEntretien'], '%d/%m/%Y')
    nb_fichiers = len(candidat['fichiers'])
    if nb_fichiers == 0:
        return 0
    else:
        nb_jours_avant_depot_moyen = 0
        for fichier in candidat["fichiers"]:
            date_depot = datetime.strptime(fichier['stats']['dateUpload'], '%d/%m/%Y')
            if date_depot != date_entretien:
                nb_jours_avant_depot_moyen += (date_depot - date_entretien).days
        return nb_jours_avant_depot_moyen/nb_fichiers



"""date1 = datetime.strptime('01/09/2018', '%d/%m/%Y')
date2 = datetime.strptime('05/09/2018', '%d/%m/%Y')
diff = date2 - date1
print(type(diff.days))"""
