import dash
import dash_core_components as dcc
import dash_html_components as html
import math as m
import pandas as pd
import flask as fl
import plotly.plotly as py
import visualizer.app.panels.auth

from plotly import graph_objs as go
from dash.dependencies import Input, Output


def getHeader(currentTab = "accueilTab"):
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
                    value=currentTab,
                    )
            ],
            className="row tabs_div"
            ),





# Tab content
            html.Div(id="tab_content", className="row", style={"margin": "2% 3%"}),

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
