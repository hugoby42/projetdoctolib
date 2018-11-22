# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

from access import getData, update

def generate_table_affichage_tout(dataframe):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe[0].keys()])] +

        # Body
        [html.Tr([
            html.Td(str(dataframe[i][col])) for col in dataframe[0].keys()
        ]) for i in range(len(dataframe))]
    )
def generate_table_affichage_nom_prenom(dataframe):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in list(dataframe[0].keys())[:3]])] +

        # Body
        [html.Tr([
            html.Td(str(dataframe[i][col])) for col in list(dataframe[0].keys())[:3]
        ]) for i in range(len(dataframe))]
    )
app.layout = html.Div([
    html.H4(children='Candidats'),
    generate_table_affichage_nom_prenom(getData()),
    html.Button(id='bouton_suppression', n_clicks=0, children='Supprimer'),
    html.Div(id='output-state')])
id_candidat=0

@app.callback(Output('output-state', 'children'),
              [Input('bouton_suppression', 'n_clicks')])

def update_output(n_clicks):
    if n_clicks ==1:
        supprimer_candidat(id_candidat)
        return "A été supprimé"
def supprimer_candidat(id_candidat):
    data=getData()
    i=0
    while data[i]['id']!=id_candidat:
        i+=1
    del data[i]
    update(data)

if __name__ == '__main__':
    app.run_server(debug=True)
