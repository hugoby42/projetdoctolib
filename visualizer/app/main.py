# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import math as m
import pandas as pd
import flask as fl
import plotly.plotly as py

from plotly import graph_objs as go
from dash.dependencies import Input, Output
from panels import candidat, login, main, management, erreur404, postuler, statistiques



logged = False



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



def launch():
    # Fonction permettant de lancer la webapp Dash multipages
    app.run_server(debug=True, port=4242)



@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def afficherPage(pathname):
    # Permet de switcher entre chaque page de la webapp

    if not logged:
        return login.layout

    elif pathname == '/login':
        # Page de login, nécessaire pour accéder à l'interface recruteur
        return login.layout

    elif pathname in ["/", "/accueil", "/index", "/main"]:
        # Page d'accueil (main)
        return main.layout

    elif pathname.startswith("/candidat/"):
        # Page personnelle concernant le candidat (le deuxième paramètre identifie le candidat)
        return candidat.layout

    elif pathname == "/management":
        # Page permettant d'afficher la liste des candidats, et de les
        # filtrer selon des critères choisis par l'utilisateur
        return manage.layout

    elif pathname == "/postuler":
        # Page permettant au candidat de déposer son dossier
        return postuler.layout

    elif pathname == "/statistiques":
        # Page permettant d'afficher l'ensemble des statistiques concernant l'ensemlbe des candidats
        return statistiques.layout

    else:
        # Page d'erreur (URL non résolue)
        return erreur404.layout


@app.callback(Output("tab_content", "children"), [Input("tabs", "value")])
def changerPage(tab):
    # Fonction permettant de changer de page lorsque l'utilisateur clique sur un tab (un des boutons du header)
    if tab == "seDeconnecter":
        confirm = dcc.ConfirmDialog(
                id='confirm',
                message="Attention. Vous allez être déconnecté de l'Interface de Recrutement Doctolib"
                )

    pathname = "/" + tab
    afficherPage(pathname)



@app.callback(dash.dependencies.Output('page-content', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('login', 'login'), dash.dependencies.State('password', 'password')])
def connecter(login, password):
    # Fonction réalisant l'authentification de l'utilisateur sur la plateforme
    global logged

    if auth.verify(login, password): # Si la connexion est réussie
        logged = True
        confirm = dcc.ConfirmDialog(
                id='confirm',
                message="Félicitations. Vous vous êtes connecté avec succès.")
        changerPage("accueil")

    logged = False # Si la connexion échoue
    confirm = dcc.ConfirmDialog(
                id='confirm',
                message="Couple login / password invalide.")
    changerPage("login")



launch() # Lancement de l'application web
