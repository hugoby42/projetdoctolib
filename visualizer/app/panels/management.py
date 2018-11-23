from visualizer.app.panels.__common__ import *
from visualizer.app.panels.statistiques import *


nb_candidats = 0

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


    nb_candidats += 1

print(nb_candidats_etape)
print(list(nb_candidats_etape.values()))
print(type(list(nb_candidats_etape.values())))


data_notes = [
        {
            'values': nb_candidats_note,
            'labels': ['★✩✩✩✩', '★★✩✩✩', '★★★✩✩', '★★★★✩', '★★★★★'],
            'type': 'pie'
        },
    ]

data_etapes = [
    {
        'values': list(nb_candidats_etape.values()),
        'labels': list(nb_candidats_etape.keys()),
        'type': 'pie'
    }
]


layout=html.Div([
    html.Div(children = [
        dcc.Graph(
            id='graph_1',
            figure={
                'data': data_etapes,
                'layout': {
                    'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
                    },
                    'legend': {'x': 0, 'y': 1}
                }
            })]
    ),
    htlm.Br(),
    htlm.H1("C'est OK !"),
    htlm.Br(),
    htlm.Div(children = [
        dcc.Graph(
            id='graph_2',
            figure={
                'data': data_notes,
                'layout': {
                    'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
                    },
                    'legend': {'x': 0, 'y': 1}
                }
            })
        ]
    ),
    htlm.H2('Tout est imprimé !!')
])


