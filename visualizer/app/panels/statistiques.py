from visualizer.app.panels.__common__ import *
import dash_html_components as htlm
import dash_core_components as dcc
from datetime import datetime
from visualizer.db.access import getData
import visualizer.app.panels.statistiques_fonctions as stat_fonction


data = getData()

'''Idées de ce qu'on pourrait faire: afficher la moyenne des notes, le nb de candidats à chaque étape, 
nb de candidats avec chaque note, nb de candidats pour chaque année de naissance, nb de jours moyens avant
le dépôt de l'exercice'''



#Cacul de la note moyenne
somme_notes = 0
nb_candidats = 0

#Nb de jours moyen entre l'entretien et le dépôt des exercices
nb_jours_moyen_entretien_depot = 0

#Nb moyen des statistiques (nb de comments, fonctions, triche, moyenne de la qualité des variables...)
nb_comments_moyen = 0
nb_fonctions_moyen = 0
qualite_variable_moyenne= 0
nb_duplicate_moyen = 0

#Répartitions des candidats selon leur note
nb_candidats_note = [0,0,0,0,0]

#Répartitions des candidats selon leur étape de recrutement
nb_candidats_etape = {}
nb_candidats_etape['Postulé'] = 0
nb_candidats_etape['Exercice donné'] = 0
nb_candidats_etape['Code en cours de vérification'] = 0
nb_candidats_etape['Fin de candidature'] = 0
nb_candidats_etape['Refus'] = 0
nb_candidats_etape['Recruté'] = 0

#Répartitions des candidats selon leur âge
age = {}
for i in range (1970,1999):
    age[str(i)] = 0

for candidat in data:
    #répartition des candidats selon leur note
    candidat_note = candidat['metrics']['level']
    nb_candidats_note[candidat_note-1] += 1

    #répartition des candidats selon leur étape
    candidat_etape = candidat['etat']
    nb_candidats_etape[candidat_etape] += 1

    #répartition des candidats selon leur âge
    date_naissance = candidat['dateNaissance'][6:]
    age[date_naissance] += 1

    #nb moyen des statistiques
    stats = stat_fonction.compteur_statistique(candidat)
    if stats != 0 :
        nb_fonctions_moyen += stats[0]
        nb_comments_moyen += stats[1]
        qualite_variable_moyenne += stats[2]
        nb_duplicate_moyen += stats[3]

    #Calcul nb de jours moyen entre l'entretien et le dépôt des exercices
    nb_jours_moyen_entretien_depot += stat_fonction.nb_jours_avant_depot(candidat)

    #calcul de la note moyenne
    somme_notes += candidat['metrics']['level']
    nb_candidats += 1

moyenne = round(somme_notes/nb_candidats,2)
nb_jours_moyen_entretien_depot = round(nb_jours_moyen_entretien_depot/nb_candidats,2)
nb_comments_moyen = round(nb_comments_moyen/nb_candidats,2)
nb_fonctions_moyen = round(nb_fonctions_moyen/nb_candidats,2)
qualite_variable_moyenne = round(qualite_variable_moyenne/nb_candidats,2)
nb_duplicate_moyen = round(nb_duplicate_moyen/nb_candidats,2)


data_notes = [
    {'values': nb_candidats_note,
     'labels': ['★✩✩✩✩', '★★✩✩✩', '★★★✩✩', '★★★★✩', '★★★★★'],
     'type': 'pie',
     'marker':{'colors': ["#264e86", "#0074e4", "#74dbef", "#eff0f4","#CFA0E9"],},
     'title':'Répartition des candidats en fonction de leur note',
     'hoverinfo': 'values+labels'}]

data_etapes = [
    {'values': list(nb_candidats_etape.values()),
     'labels': list(nb_candidats_etape.keys()),
     'type': 'pie',
     'marker':{'colors': ["#264e86", "#0074e4", "#74dbef", "#eff0f4","#CFA0E9"]},
     'title': 'Répartition des candidats en fonction de leur étape de recrutement'}]

#Affichage de la page Statistiques
colors = {'background': '#FFFFFF', 'text': '#000000', 'contour' : '#2E3F5C'}

layout = html.Div(
    children=[
        htlm.H1('Statistiques'),
        html.Div(
            htlm.Div(
                children=[
                    "Nombre de candidats :{}".format(nb_candidats), htlm.Br(),
                    'Moyenne des notes = {}'.format(moyenne), htlm.Br()
                ],
                style={
                    'backgroundColor': colors['background']},
                className='six columns'),
            className='row'),
        htlm.Br(),
        htlm.Div(
            children = [
                "Nombre de jours moyen entre l'entretien et le dépôt : {}".format(nb_jours_moyen_entretien_depot), htlm.Br(),
                "Nombre moyen de commentaires par fichier : {}".format(nb_comments_moyen), htlm.Br(),
                "Nombre moyen de fonctions par fichiers : {}".format(nb_fonctions_moyen), html.Br(),
                "Qualité moyenne des variables : {}%".format(qualite_variable_moyenne*100), htlm.Br(),
                "Nombre moyen de triche : {}".format(nb_duplicate_moyen), htlm.Br()],
            style={
                    'backgroundColor': colors['background']}
        ),
        htlm.Br(),
        htlm.Div([
            dcc.Graph(
                id = 'graph_3_Répartiton date naissance',
                figure={
                    'data': [{'x':list(age.keys()),'y': list(age.values()),
                              'type':'bar', 'name':'age'
                              }],
                    'layout':{'title': 'Répartition des candidats en fonction de leur date de naissance'}}
            )
        ]),
        htlm.Br(),
        html.Div(children = [
        dcc.Graph(
            id='graph_1, Répartition en fonction des notes',
            figure={
                'data': data_notes,
                'layout': {
                    'margin': {'l': 30, 'r': 0, 'b': 30, 't': 0},
                    'legend': {'x': 0, 'y': 1}},
            },
        )
    ]),
        htlm.Br(),
        htlm.Div(children = [
        dcc.Graph(
            id='graph_2, Répartition en fonction des étapes',
            figure={
                'data': data_etapes,
                'layout': {
                    'margin': {'l': 30,'r': 0,'b': 30,'t': 0},
                    'legend': {'x': 0, 'y': 1}}
            })
    ]),
    ]
)
