from visualizer.app.panels.__common__ import *
import visualizer.db.access as access
import os
from visualizer.app.panels.management import get_id_candidat
#le candidat conserné
id_candidat=get_id_candidat()
#importer les données du candidat
data=access.getData()
data_candidat=data[id_candidat]

###Stats du candidat

fichiers=data_candidat['fichiers']
nb_fichier = len(fichiers)
nb_fonctions_tot = 0
nb_comment_tot = 0
var_quality_tot = 0
nb_cheat_tot = 0
for fichier in fichiers:
    nb_fonctions = fichier['stats']['functionsCount']
    nb_comment = fichier['stats']['commentCount']
    var_quality = fichier['stats']['variableNameQuality']
    nb_cheat = len(fichier['stats']['duplicate'])
    nb_fonctions_tot += nb_fonctions
    nb_comment_tot += nb_comment
    var_quality_tot += var_quality/nb_fichier
    nb_cheat_tot +=nb_cheat
var_quality_tot=str(int(round(var_quality_tot,2)*100))+'%'
###


colors = {
    'background': '#FFFFFF',
    'text': '#000000',
    'contour' : '#2E3F5C'
}



###
stat_table=[['Nombre de fichiers',nb_fichier],
       ['Nombre de fonctions',nb_fonctions_tot],
       ['Nombre de commentaires',nb_comment_tot],
       ['Qualité du nom des variables',var_quality_tot],
       ['Nombre de simmilarités avec notre base de donneés',nb_cheat_tot]]


###TABLES
def make_dash_table(table):
    ''' Return a dash definition of an HTML table for a Pandas dataframe '''
    html_table=[]
    for row in table:
        html_row=[]
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        html_table.append(html.Tr(html_row))
    return html_table

###FICHIERS
options_file=[]
for fichier in data_candidat['fichiers']:
    options_file.append({'label': 'Fichier ' + fichier['id'], 'value': 'fichier-'+fichier['id']})
options_test=[]
for fichier in data_candidat['fichiers']:
    options_test.append({'label': 'Test ' + fichier['id'], 'value': 'fichier-test-'+fichier['id']})
###


#### NIVEAU DU CANDIDAT
etoile_vide='✩'
etoile_pleine='★'
def niveau_candidat(data_candidat):
    level=data_candidat['metrics']['level']
    return etoile_pleine*level+etoile_vide*(5-level)
###

###Etat candidat
etats=['Postulé','Exercice donné','Code en cours de vérification','Fin de candidature','Refus','Recruté']
options_etat=[]
for etat in etats:
    options_etat.append({'label' : etat, 'value' : etat})
###

###Suppression candidat
def update_output(n_clicks):
    if n_clicks ==1:
        supprimer_candidat(id_candidat)
        print("ok")
        return "A été supprimé"
def supprimer_candidat(id_candidat):
    data=access.getData()
    i=0
    while data[i]['id']!=id_candidat:
        i+=1
    del data[i]
    access.update(data)




layout = html.Div([  # page 1



        html.Div(style={'textAlign': 'center'},children = [
            html.H1(data_candidat['nom'] + ' ' + data_candidat['prenom'],
                            className="gs-header gs-text-header padded"),

            # Row 1
            html.Div([

                html.Div(style={'backgroundColor': colors['background'],
                                'textAlign': 'left',
                                "border": "1px solid " + colors['contour'],
                                "paddingLeft" : '4',
                                "paddingBottom" : '21'}, children = [
                    html.H6(['Informations personnelles'],
                            className="gs-header gs-text-header padded"),

                   "Date de naissance : " + data_candidat['dateNaissance'],
                    html.Br([]),
                    "Lieu de naissance : " + data_candidat['lieuNaissance'],
                    html.Br([]),
                    "Date d'entretien : " + data_candidat['dateEntretien'],
                    html.Br([]),
                    "Lieu d'entretien : " + data_candidat['lieuEntretien'],

                ], className="six columns",),

                html.Div(style={'backgroundColor': colors['background'],
                                "border": "1px solid "+ colors['contour'],
                                "paddingLeft" : '4'}, children = [
                    html.H6(["Statistiques du candidat"],
                            className="gs-header gs-table-header padded"),
                        html.Table(make_dash_table(stat_table)),
                ], className="six columns"),

            ], className="row "),
            #Row 2
        html.Div(children=[
            html.Div(style={'marginTop' : '10',
                        'backgroundColor': colors['background'],
                         "border": "1px solid "+ colors['contour'],},children=[
                html.H6(["Candidature pour Doctolib"],
                        className="gs-header gs-table-header padded"),
                html.P(id='etat-content',children=['Etat : ' + data_candidat['etat']]),
                html.Br(),
                html.P('Niveau du candidat : ' + niveau_candidat(data_candidat)),
            ],className="six columns"),
            html.Div(style={'marginTop' : '10',
                        'backgroundColor': colors['background'],
                         "border": "1px solid "+ colors['contour'],},children=[
                        html.H6(["Modifier l'état du candidat"],
                        className="gs-header gs-table-header padded"),
                        dcc.Dropdown(
                        options=options_etat,
                        id="etat-dropdown",
                        value=data_candidat['etat']
                    )
            ],className="six columns")
        ],
        className="row "),
            #Rox 3
        html.Div(style={'marginTop' : '10'},children=[
            html.Div([
            dcc.Dropdown(
                    options=options_file,
                    id="fichiers-dropdown",
                    value='neutre'
                    ),
                html.Div(id='fichiers-content',style={'marginTop' : '10',
                                                      'backgroundColor': colors['background'],
                                                        "border": "1px solid "+ colors['contour'],}
                         , children=[html.Div([])])
                ])
        ],
        className="row "),
        html.Div(style={'marginTop' : '10'},children=[
            html.Div([
            dcc.Dropdown(
                    options=options_test,
                    id="fichiers-test-dropdown",
                    value='neutre'
                    ),
                html.Div(id='tests-content',style={'marginTop' : '10',
                                                      'backgroundColor': colors['background'],
                                                        "border": "1px solid " + colors['contour'],}
                         , children=[])
                ])
        ],
        className="row "),
        html.Div(style={'marginTop' : '10'},children=[
            html.Div([


            ])
        ],
        className="row "),
            html.Div(style={'marginTop' : '10'},children=[
            html.Button(id='bouton_suppression', n_clicks=0, children='Supprimer le candidat'),
            html.Div(id='output-state')
        ],
        className="row "),

        ], className="subpage")

    ], className="page")

@app.callback(Output('fichiers-content', 'children'),
              [Input('fichiers-dropdown', 'value')])
def affiche_fichier(fichiersdropdown):
    print("Hzsfzsfe")
    for fichier in data_candidat['fichiers']:
        if fichiersdropdown == 'fichier-'+fichier['id']:
            return html.Div(html.Div([
                html.H3(fichier['nom']),
                html.P(fichier['contenu'],style={'backgroundColor': '#BBD2E1'}),
                "Date d'upload : " + fichier['stats']['dateUpload'],
                html.Br(),
                "Commentaire sur le code : " + fichier['stats']['compteRendu'],
                html.Br(),
                "Nombre de fonctions : " + str(fichier['stats']['functionsCount']),
                html.Br(),
                "Nombre de commentaires : " + str(fichier['stats']['commentCount']),
                html.Br(),
                "Qualité du nom des variables : " + str(int(round(fichier['stats']['variableNameQuality'],2)*100))+'%',
                html.Br(),
                "Nombre de similaritées avec notre base de données : " + str(len(fichier['stats']['duplicate'])),

            ]))
@app.callback(Output('tests-content', 'children'),
              [Input('fichiers-test-dropdown', 'value')])
def affiche_test(fichierstestdropdown):
    print("Hzsfzsfe")
    for fichier in data_candidat['fichiers']:
        if fichierstestdropdown == 'fichier-test-'+fichier['id']:
            return html.Div([
                html.H3(fichier['nomTest']),
                html.P(fichier['contenu_Test'],style={'backgroundColor': '#BBD2E1'}),
            ])

@app.callback(Output('etat-content','children'),
              [Input('etat-dropdown','value')])

def update_database(etatdropdown):
    data_candidat['etat']=etatdropdown
    data[id_candidat]=data_candidat
    directory=os.getcwd()
    if directory[len(directory)-10:]=='visualizer':
        os.chdir('./db')
    elif directory[len(directory)-3:]=='app':
        os.chdir('../')
        os.chdir('.db')
    elif directory[len(directory)-6:]=='panels':
        os.chdir('../../')
        os.chdir('./db')
    visualizer.db.access.update(data, fileName = "input.json")
