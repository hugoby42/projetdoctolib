# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from access import getData

data=getData()

nb_candidats_dans_etat=[0,0]
for i in data:
    if i['fichiers']==[]:
        nb_candidats_dans_etat[0]+=1
    else:
        nb_candidats_dans_etat[1]+=1
"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.........
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ['Code non réceptionné', 'Code réceptionné'], 'y': nb_candidats_dans_etat, 'type': 'bar', 'name': "Etat d'avancement du candidat"},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

"""

def generate_table(dataframe):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe[0].keys()])] +

        # Body
        [html.Tr([
            html.Td(str(dataframe[i][col])) for col in dataframe[0].keys()
        ]) for i in range(len(dataframe))]
    )



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='Candidats'),
    generate_table(data)
])

if __name__ == '__main__':
    app.run_server(debug=True)


