# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from access import getData

data=getData()
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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='Candidats'),
    generate_table_affichage_nom_prenom(data)
])

if __name__ == '__main__':
    app.run_server(debug=True)
