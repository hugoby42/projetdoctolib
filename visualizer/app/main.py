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



DASH_APP_NAME = 'Interface Recrutement Doctolib' # Informations concernant le serveur Dash 
DASH_APP_PRIVACY = 'public' # Il est possible pour n'importe quel utilisateur de se connecter sur Dash
PATH_BASED_ROUTING = True



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] # Feuilles de style CSS utilisées (template)
app = dash.Dash("Interface Recrutement Doctolib") # Création de l'application web
app.config.supress_callback_exceptions = True 
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

                    dcc.Tab(label="Se Déconnecter", value="seDeconnecter"),

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



def launch():
    # Fonction permettant de lancer la webapp Dash multipages
    app.run_server(debug=True, port=4242)



app.layout = getHeader()



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

    elif pathname.startswith("/candidat"):
        # Page personnelle concernant le candidat (le deuxième paramètre identifie le candidat)
        return candidat.layout

    elif pathname == "/management":
        # Page permettant d'afficher la liste des candidats, et de les
        # filtrer selon des critères choisis par l'utilisateur
        return management.layout

    elif pathname == "/postuler":
        # Page permettant au candidat de déposer son dossier
        return postuler.layout

    elif pathname == "/statistiques":
        # Page permettant d'afficher l'ensemble des statistiques concernant l'ensemlbe des candidats
        return statistiques.layout

    else:
        # Page d'erreur (URL non résolue)
        return erreur404.layout



launch() # Lancement de l'application web
