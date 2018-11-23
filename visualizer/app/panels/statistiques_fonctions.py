from datetime import datetime
from visualizer.db.access import getData


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


def compteur_statistique(candidat):
    nb_fichiers=len(candidat['fichiers'])
    if nb_fichiers == 0:
        return 0
    nb_fonctions=0
    nb_comments=0
    qualite_variable=0
    nb_duplicate=0
    for fichier in candidat['fichiers']:
        stats = fichier['stats']
        nb_fonctions += stats['functionsCount']
        nb_comments += stats['commentCount']
        qualite_variable += stats['variableNameQuality']
        nb_duplicate += len(stats['duplicate'])
    return [nb_fonctions/nb_fichiers, nb_comments/nb_fichiers, qualite_variable/nb_fichiers, nb_duplicate/nb_fichiers]

"""date1 = datetime.strptime('01/09/2018', '%d/%m/%Y')
date2 = datetime.strptime('05/09/2018', '%d/%m/%Y')
diff = date2 - date1
print(type(diff.days))"""
