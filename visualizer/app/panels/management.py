from app.panels.__common__ import *

def make_dash_table(table):
    ''' Return a dash definition of an HTML table from the dataframe '''
    html_table=[]
    html_table.append(html.Tr(style={'fontSize' : '20'},children=[html.Td(['id']),html.Td('Nom'),html.Td('Prénom'),html.Td('Niveau'),html.Td('Candidature')]))
    for candidat in table:
        html_row=[]
        html_row.append(html.Td([candidat['id']]))
        html_row.append(html.Td([candidat['nom']]))
        html_row.append(html.Td([candidat['prenom']]))
        html_row.append(html.Td([candidat['metrics']['level']]))
        html_row.append(html.Td([candidat['etat']]))
        html_row.append(html.Td(html.Div(style={'marginTop' : '10'},children=[
                                html.Button(id='bouton_candidat'+str([candidat['id']]), n_clicks=0, children='Accéder au candidat'),
                                html.Div(id='output-state')
        ],
        className="row "),
))
        html_table.append(html.Tr(html_row))
    return html_table

def trier_par_level():
    """Trie la table en fonction du niveau"""
    data = db.access.getData()
    data_triee=[{} for i in range(len(data))]
    liste_nom=[[data[i]['metrics']['level'],data[i]['id']] for i in range(len(data))]
    liste_nom=sorted(liste_nom)
    for i in range(len(liste_nom)):
        data_triee[i]=data[liste_nom[i][1]]
    return(data_triee)
###TRER etat,nom,prenom

def trier_par(type):
    """Trie la table en fonction de l'entrée type, colonne de la table"""
    data = db.access.getData()
    data_triee=[{} for i in range(len(data))]
    liste_nom=[[data[i][type],data[i]['id']] for i in range(len(data))]
    liste_nom=sorted(liste_nom)
    for i in range(len(liste_nom)):
        data_triee[i]=data[liste_nom[i][1]]
    return(data_triee)

def getManagement():
    data=db.access.getData()
    ####TABLE
    def make_dash_table(table):
        ''' Return a dash definition of an HTML table from the dataframe '''
        html_table=[]
        html_table.append(html.Tr(style={'fontSize' : '20'},children=[html.Td(['id']),html.Td('Nom'),html.Td('Prénom'),html.Td('Niveau'),html.Td('Candidature')]))
        for candidat in table:
            html_row=[]
            html_row.append(html.Td([candidat['id']]))
            html_row.append(html.Td([candidat['nom']]))
            html_row.append(html.Td([candidat['prenom']]))
            html_row.append(html.Td([candidat['metrics']['level']]))
            html_row.append(html.Td([candidat['etat']]))
            html_row.append(html.Td(html.Div(style={'marginTop' : '10'},children=[
                                    html.Button(id='boutonCandidat'+str([candidat['id']]), n_clicks=0, children='Accéder au candidat'),
                                    html.Div(id='output-state')
            ],
            className="row "),
    ))
            html_table.append(html.Tr(html_row))
        return html_table
        ###
    def get_id_candidat():
        return (0)

    ##TRIER LEVEL
    def trier_par_level(data=db.access.getData()):
        """Trie la table en fonction du niveau"""
        data_triee=[{} for i in range(len(data))]
        liste_nom=[[data[i]['metrics']['level'],data[i]['id']] for i in range(len(data))]
        liste_nom=sorted(liste_nom)
        for i in range(len(liste_nom)):
            data_triee[i]=data[liste_nom[i][1]]
        return(data_triee)
    ###TRER etat,nom,prenom

    def trier_par(type,data=db.access.getData()):
        """Trie la table en fonction de l'entrée type, colonne de la table"""
        data_triee=[{} for i in range(len(data))]
        liste_nom=[[data[i][type],data[i]['id']] for i in range(len(data))]
        liste_nom=sorted(liste_nom)
        for i in range(len(liste_nom)):
            data_triee[i]=data[liste_nom[i][1]]
        return(data_triee)
    ###
    colors = {
        'background': '#FFFFFF',
        'text': '#000000',
        'contour' : '#2E3F5C'
    }

    ###LABELS DE TRI
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


                ], className="row "),
                html.Div([

                    html.Div(id='tri-content',children = [
                        html.Table(make_dash_table(data)),
                    ],),

                ], className="row "),
            ], className="subpage")

        ], className="page")
            ])

    return layout
