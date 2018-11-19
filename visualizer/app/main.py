# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import math
import pandas as pd
import flask
import plotly.plotly as py
import postuler

from plotly import graph_objs as go
from dash.dependencies import Input, Output
from panels import candidat, login, main, manage, erreur404, postuler


DASH_APP_NAME = 'Interface Recrutement Doctolib'
DASH_APP_PRIVACY = 'public'
PATH_BASED_ROUTING = True

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash("hub")
server = app.server()
app.config.supress_callback_exceptions = True

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def afficher(pathname):
    # Permet de switcher entre chaque page de la webapp

    if pathname == '/login': # Page de login, nécessaire pour accéder à l'interface recruteur
        return login.layout
    elif pathname.startswith"/candidat/": # Page personnelle concernant le candidat (le deuxième paramètre identifie le candidat)
        return candidat.layout
    elif pathname == "/": # Page d'accueil (main)
        return main.layout
    elif pathname == "/manage": # Page permettant d'afficher la liste des candidats, et de les filtrer selon des critères choisis par l'utilisateur
        return manage.layout
    elif pathname == "/postuler": # Page permettant au candidat de déposer son dossier
        return postuler.layout
    else: # Page d'erreur
        return erreur404.layout

def launch():
    # Fonction permettant de lancer la webapp Dash multipages
    app.run_server(debug=True)
