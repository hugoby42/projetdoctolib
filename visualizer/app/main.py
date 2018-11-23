# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import math as m
import pandas as pd
import flask as fl
import plotly.plotly as py

from plotly import graph_objs as go
from dash.dependencies import Input, Output, State
from app.panels import candidat, login, main, management, erreur404, postuler, statistiques
from app.app import *
import db.access
import db.gen



DASH_APP_NAME = 'Interface Recrutement Doctolib' # Informations concernant le serveur Dash 
DASH_APP_PRIVACY = 'public' # Il est possible pour n'importe quel utilisateur de se connecter sur Dash
PATH_BASED_ROUTING = True



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] # Feuilles de style CSS utilisées (template)
app = dash.Dash("Interface Recrutement Doctolib") # Création de l'application web
app.config['supress_callback_exceptions']= True



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

def getHeader():
    header = html.Div(
            [
# header
            html.Div([
                html.Span([html.I("school", className="material-icons md-light", style={"verticalAlign":"middle"}), " Interface de Recrutement - Doctolib H.R."], className='app-title'),

                html.Div(
                    html.Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Logo-doctolib-bleu-tr_%28crop%29.png/640px-Logo-doctolib-bleu-tr_%28crop%29.png',height="100%")
                    ,style={"float":"right","height":"100%"})
            ],
            className="row header"
            ),


            html.Div([
                dcc.Tabs(
                    id="tabs",
                    style={"height":"20","verticalAlign":"top"},
                    children=[
                    dcc.Tab(label="Accueil", value="accueil"),
                    dcc.Tab(label="Management", value="management"),
                    dcc.Tab(label="Candidat", value="candidat"),
                    dcc.Tab(label="Statistiques", value="statistiques"),
                    dcc.Tab(label="Postuler", value="postuler")
                    ],
                    value="neutre",
                    )
            ],
            className="row tabs_div"
            ),



# Tab content
            html.Div(id="corps", className="row", style={"margin": "2% 3%"}),

            html.Link(href="https://use.fontawesome.com/releases/v5.2.0/css/all.css",rel="stylesheet"),
            html.Link(href="https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css",rel="stylesheet"),
            html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
            html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
            html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
            html.Link(href="https://cdn.rawgit.com/amadoukane96/8a8cfdac5d2cecad866952c52a70a50e/raw/cd5a9bf0b30856f4fc7e3812162c74bfc0ebe011/dash_crm.css", rel="stylesheet")
            ,
            html.Link(href="https://fonts.googleapis.com/icon?family=Material+Icons", rel="stylesheet")
            ],
            className="row",
            style={"margin": "0%"}
            )
    return header

app.layout = getHeader()

def launch():
    # Fonction permettant de lancer la webapp Dash multipages
    app.run_server(debug=True, port=4012)



@app.callback(Output('corps', 'children'),
              [Input('tabs', 'value')])
def afficherPage(tab):
    # Permet de switcher entre chaque page de la webapp
    
    if tab == "seDeconnecter":
        confirm = dcc.ConfirmDialog(
                id='confirm',
                message="Attention. Vous allez être déconnecté de l'Interface de Recrutement Doctolib"
                )

    pathname = "/" + tab


    """if not logged:
        return login.layout"""

    if pathname == '/login':
        # Page de login, nécessaire pour accéder à l'interface recruteur
        return login.layout

    elif pathname in ["/", "/accueil", "/index", "/main"]:
        # Page d'accueil (main)
        print("topito")
        return main.layout

    elif pathname.startswith("/candidat/"):
        # Page personnelle concernant le candidat (le deuxième paramètre identifie le candidat)
        return candidat.getCandidat(2)

    elif pathname.startswith("/candidat"):
        # Page personnelle concernant le candidat (le deuxième paramètre identifie le candidat)
        return candidat.getCandidat()

    elif pathname == "/management":
        # Page permettant d'afficher la liste des candidats, et de les
        # filtrer selon des critères choisis par l'utilisateur
        return management.getManagement()

    elif pathname == "/postuler":
        # Page permettant au candidat de déposer son dossier
        return postuler.layout

    elif pathname == "/statistiques":
        # Page permettant d'afficher l'ensemble des statistiques concernant l'ensemlbe des candidats
        return statistiques.layout

    else:
        # Page d'erreur (URL non résolue)
        return erreur404.layout
"""
@app.callback(Output('fichiers-content', 'children'),
              [Input('fichiers-dropdown', 'value')])
def affiche_fichier(fichiersdropdown):
    print("Hzsfzsfe")
    for fichier in data_candidat['fichiers']:
        if fichiersdropdown == 'fichier-'+fichier['id']:
            return html.Div(html.Div([
                html.H3(fichier['nom']),
                affiche_pretty_fichier(fichier['contenu']),
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
    # Fonction assurant l'affichage d'un fichier test
    
    for fichier in data_candidat['fichiers']:
        if fichierstestdropdown == 'fichier-test-'+fichier['id']:
            return html.Div([
                html.H3(fichier['nomTest']),
                affiche_pretty_fichier(fichier['contenu_Test']),
            ])


@app.callback(Output('etat-content','children'),
              [Input('etat-dropdown','value')])
def update_database(etatdropdown):
    # Fonction permettant de mettre à jour l'état d'un candidt

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
    db.access.update(data, fileName = "input.json")
"""

@app.callback(Output('tri-content', 'children'),
              [Input('tri-dropdown', 'value')])
def callback_trier_candidat(value):
    # Fonction pemettant de trier le dataTable en fonction d'un critère donné
    if value == 'nom':
        return html.Table(management.make_dash_table(management.trier_par('nom')))
    elif value == 'prenom':
        return html.Table(management.make_dash_table(management.trier_par('prenom')))
    elif value == 'etat':
        return html.Table(management.make_dash_table(management.trier_par('etat')))
    elif value == 'level':
        return html.Table(management.make_dash_table(management.trier_par_level()))
    else:
        return html.Table(management.make_dash_table(management.trier_par('id')))

@app.callback(Output("candidature", "style"), [Input("candidater", "n_clicks")])
def display_leads_modal_callback(n):
    # Fonction permettant d'afficher une fenêtre modale d'inscription
    if n > 0:
        return {"display": "block"} # On fait apparaître la fenêtre modale

    return {"display": "none"} # On la fait disparaître


"""
def getCandidatCallback(id):
    return candidat.getCandidat(id.split("boutonCandidat")[1])

data = db.access.getData()
for candidat in data:
    app.callback(Output("tabs", "value"), [Input("boutonCandidat"+str([candidat['id']]))])(getCandidatCallback(id))
"""


@app.callback(Output("candidater", "n_clicks"), [Input("leads_modal_close", "n_clicks"), Input("postuler", "n_clicks")])
def close_modal_callback(n, n2):
    # Fonction permettant de fermer la fenêtre modale d'inscription

    return 0


@app.callback(
    Output('zorimar', 'children'),
    [Input('postuler', 'n_clicks')],
    [State('prenomPostuler', 'value'),
     State('nomPostuler', 'value'),
     State('lieuNaissancePostuler', 'value'),
     State('niveauPostuler', 'value')])
def update_output(n_clicks, prenom, nom, lieuNaissance, niveau):
    data = db.access.getData()
    idCandidat = len(data)
    candidat = db.gen.creation_candidat(idCandidat, idCandidat)
    candidat["prenom"] = prenom
    candidat["nom"] = nom
    candidat["lieuNaissance"] = lieuNaissance
    candidat["etat"] = "Postulé"
    candidat["metrics"]["level"] = niveau
    data.append(candidat)
    db.access.update(data)
    return []

"""
@app.callback(Output('steveJobs', 'text'),
              [Input('etatCandidat', 'value'), Input('supprimerCandidat', 'n_clicks')], [State('steveJobs', 'value')])
def changerEtatCandidat(etatCandidat, n_clicks, idCandidat):
    if n_clicks > 0:
        print("hey")
        data = db.access.getData()
        data[int(idCandidat)]["etat"] = etatCandidat
        db.access.update(data)

def aSupprimer(candidat, id):
    return (candidat["id"] == id)

@app.callback(Output('steveJobs', 'children'),
              [Input('supprimerCandidat', 'n_clicks')], [State('steveJobs', 'value')])
def supprimerCandidat(n_clicks, idCandidat):
    if n_clicks > 0:
        print("ho")
        data = db.access.getData()
        #index = filter(aSupprimer, idCandidat)
        data.pop(int(idCandidat))
        db.access.update(data)
"""
