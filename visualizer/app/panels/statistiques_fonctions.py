from datetime import datetime


# fonction qui calcule le nb de jours moyen entre l'entretien et le dépôt pour un candidat

def nb_jours_avant_depot(candidat):
    # on transforme les chaînes de caractères en objets datetime
    date_entretien = datetime.strptime(candidat['dateEntretien'], '%d/%m/%Y')
    
    nb_fichiers = len(candidat['fichiers'])
    # s'il n'y a pas de fichier, on renvoit 0
    if nb_fichiers == 0:
        return 0
    
    else:
        nb_jours_avant_depot_moyen = 0
        # On fait la moyenne du nb de jours entre l'entretien et le dépôt d'un exercice par fichier pour le candidat
        for fichier in candidat["fichiers"]:
            date_depot = datetime.strptime(fichier['stats']['dateUpload'], '%d/%m/%Y')
            if date_depot != date_entretien:
                nb_jours_avant_depot_moyen += (date_depot - date_entretien).days
        return nb_jours_avant_depot_moyen/nb_fichiers


# Fonction effectuant les statistiques selon chacun des aspects utilisés pour les statistiques (i.e. le nb de fonctions,
# de commentaires, de fraudes, et la moyenne de la qualité des variables)

def compteur_statistique(candidat):
    # si le candidat n'a fourni aucun fichier, on renvoie 0
    nb_fichiers=len(candidat['fichiers'])
    if nb_fichiers == 0:
        return 0
    
    # sinon, on fait la moyenne de chaque caractéristique par fichier pour le candidat
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
