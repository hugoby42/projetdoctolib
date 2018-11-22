from visualizer.app.panels.__common__ import *
import visualizer.db.access as access

data=access.getData()
table=data
####TABLE
def make_dash_table(table):
    ''' Return a dash definition of an HTML table for a Pandas dataframe '''
    html_table=[]
    html_table.append(html.Tr(style={'fontSize' : '20'},children=[html.Td(['id']),html.Td('Nom'),html.Td('Prénom'),html.Td('Niveau'),html.Td('Candidature')]))
    for candidat in table:
        html_row=[]
        html_row.append(html.Td([candidat['id']]))
        html_row.append(html.Td([candidat['nom']]))
        html_row.append(html.Td([candidat['prenom']]))
        html_row.append(html.Td([candidat['metrics']['level']]))
        html_row.append(html.Td([candidat['etat']]))
        html_table.append(html.Tr(html_row))
    return html_table
###
def get_id_candidat():
    return (0)
###
colors = {
    'background': '#FFFFFF',
    'text': '#000000',
    'contour' : '#2E3F5C'
}

###TRIER
options=[
    {'label' : 'par identifiant', 'value' : 'id'},
    {'label' : 'par nom', 'value' : 'nom'},
    {'label' : 'par prénom', 'value' : 'prenom'},
    {'label' : 'par niveau', 'value' : 'level'},
    {'label' : 'par état de candidature', 'value' : 'etat'}
]



###
layout = html.Div([  # page 1



        html.Div(children = [

            # Row 1
            html.Div([

                html.Div(children = [
                    html.H3(style={'paddingLeft' : '10',
                                   'backgroundColor': colors['background'],
                                   "border": "1px solid "+ colors['contour'],},children=['Trier par :'],className="two columns"),
                    dcc.Dropdown(
                    options=options,
                    id="tri-dropdown",
                    value='id'
                    ),
                html.Div(id='tri-content',style={'marginTop' : '10',
                                                      'backgroundColor': colors['background'],
                                                        "border": "1px solid "+ colors['contour'],}
                         , children=[])
                ],),

            ], className="row "),
            html.Div([

                html.Div(children = [
                    html.Table(make_dash_table(table)),
                ],),

            ], className="row "),
        ], className="subpage")

    ], className="page")


