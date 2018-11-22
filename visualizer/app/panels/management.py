from app.panels.__common__ import *

layout = html.Div([
    ])


app.layout = html.Div([
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
