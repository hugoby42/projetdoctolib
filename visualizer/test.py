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
from panels import candidat, login, main, management, erreur404, postuler, statistiques
from app import app, logged



DASH_APP_NAME = "Interface Recrutement Doctolib" # Informations concernant le serveur Dash
DASH_APP_PRIVACY = "public" # Il est possible pour n"importe quel utilisateur de se connecter sur Dash
PATH_BASED_ROUTING = True



app.layout = html.Div([
   dcc.Location(id="url", refresh=False),
   html.Div(id="page-content")
])



def launch():
   # Fonction permettant de lancer la webapp Dash multipages
   app.run_server(debug=True, port=4242)



@app.callback(Output("page-content", "children"),
             [Input("url", "pathname"), Input("tab", "value"), Input("loginButton", "n_clicks")],
             [State("login", "login"), State("password", "password")])
def afficherPage(pathname, tab, n_clicks, login, password):
   global logged
   # Permet de switcher entre chaque page de la webapp

   if tab == "seDeconnecter":
       confirm = dcc.ConfirmDialog(
               id="confirm",
               message="Attention. Vous allez être déconnecté de l'Interface de Recrutement Doctolib")
       return login.layout



   pathname = "/" + tab

   if not logged:
       if auth.verify(login, password): # Si la connexion est réussie
           logged = True
           confirm = dcc.ConfirmDialog(
               id="confirm",
               message="Félicitations. Vous vous êtes connecté avec succès.")
           return main.layout


       confirm = dcc.ConfirmDialog(
               id="confirm",
               message="Vous n'êtes pas identifié sur la plateforme")

       return login.layout

   elif pathname == "/login":
       # Page de login, nécessaire pour accéder à l"interface recruteur
       return login.layout

   elif pathname in ["/", "/accueil", "/index", "/main", "/principal", "/lobby", "/hub", "/neutre"]:
       # Page d"accueil (main)
       return main.layout

   elif pathname.startswith("/candidat"):
       # Page personnelle concernant le candidat (le deuxième paramètre identifie le candidat)
       return candidat.layout

   elif pathname == "/management":
       # Page permettant d"afficher la liste des candidats, et de les
       # filtrer selon des critères choisis par l"utilisateur
       return manage.layout

   elif pathname == "/postuler":
       # Page permettant au candidat de déposer son dossier
       return postuler.layout

   elif pathname == "/statistiques":
       # Page permettant d"afficher l"ensemble des statistiques concernant l"ensemlbe des candidats
       return statistiques.layout

   else:
       # Page d"erreur (URL non résolue)
       return erreur404.layout
