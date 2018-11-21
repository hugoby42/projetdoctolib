from visualizer.app.panels.__common__ import *

layout = html.Div([
    getHeader(),
    html.Div([
    html.Div(dcc.Input(id='login', type='text')),
    html.Div(dcc.Input(id='password', type='text')),
    html.Button('Submit', id='connexion')
       ])
    ])
