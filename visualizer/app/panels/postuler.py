from app.panels.__common__ import *

def modal(): # Fonction renvoyat le corps de la modale servant à l'inscription d'un candidat
    return html.Div(
        html.Div(
            [
                html.Div(
                    [


                    html.Div(
                        [
                        html.Span(
                            "1. Coordonnées",
                            style={
                            "color": "#506784",
                            "fontWeight": "bold",
                            "fontSize": "20",
                            },
                            ),
                        html.Span(
                            "×",
                            id="leads_modal_close",
                            n_clicks=0,
                            style={
                            "float": "right",
                            "cursor": "pointer",
                            "marginTop": "0",
                            "marginBottom": "17",
                            },
                            ),
                        ],
                        className="row",
                        style={"borderBottom": "1px solid #C8D4E3"},
                        ),




                        html.Div(
                                [
                                html.P(
                                    "Prénom :",
                                    style={
                                    "float": "left",
                                    "marginTop": "14",
                                    "marginBottom": "2",
                                    },
                                    className="row"
                                    ),
                                dcc.Input(
                                    id="prenomPostuler",
                                    placeholder="Entrez votre prénom ...",
                                    type="text",
                                    value="",
                                    style={"width": "100%"}
                                    ),


                                html.P(
                                        "Nom :",
                                        style={
                                        "textAlign": "left",
                                        "marginBottom": "2",
                                        "marginTop": "14",
                                        }
                                      ),
                                dcc.Input(
                                        id="nomPostuler",
                                        placeholder="Entrez votre nom ...",
                                        type="text",
                                        value="",
                                        style={"width": "100%"}
                                        ),


                                html.P(
                                        "Lieu de naissance :",
                                        style={
                                        "textAlign": "left",
                                        "marginBottom": "2",
                                        "marginTop": "14",
                                        }
                                      ),
                                dcc.Input(
                                        id="lieuNaissancePostuler",
                                        placeholder="Entrez votre lieu de naissance ...",
                                        type="text",
                                        value="",
                                        style={"width": "100%"}
                                        ),


                                html.P(
                                        "Email :",
                                        style={
                                        "float": "left",
                                        "marginTop": "14",
                                        "marginBottom": "2",
                                        },
                                        className="row"
                                      ),
                                dcc.Input(
                                        id="emailPostuler",
                                        placeholder="Entrez votre email ...",
                                        type="text",
                                        value="",
                                        style={"width": "100%"}
                                        ),


                                html.P(
                                        "Téléphone :",
                                        style={
                                        "float": "left",
                                        "marginTop": "14",
                                        "marginBottom": "2",
                                        },
                                        className="row"
                                      ),
                                dcc.Input(
                                        id="telephonePostuler",
                                        placeholder="Entrez votre numéro de téléphone ...",
                                        type="text",
                                        value="",
                                        style={"width": "100%"}
                                        ),


                                html.P(
                                        "Date de naissance :",
                                        style={
                                        "textAlign": "left",
                                        "marginBottom": "2",
                                        "marginTop": "14",
                                        }
                                      ),
                                dcc.DatePickerSingle(
                                        id='dateNaissancePostuler',
                                        date=dt(2001, 8, 2)
                                        ),






                                html.Div(
                                        [
                                        html.Span(
                                            "2. Compétences",
                                            style={
                                            "color": "#506784",
                                            "fontWeight": "bold",
                                            "fontSize": "20",
                                            }
                                            )
                                        ],
                                        className="row",
                                        style={"borderBottom": "1px solid #C8D4E3", "marginTop":"75"},
                                        ),


                                        html.P(
                                                "Domaines de prédlicetion :",
                                                style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "14",
                                                }
                                              ),
                                        dcc.Dropdown(
                                                options=[
                                                {'label': 'HTM5', 'value': 'NYC'},
                                                {'label': 'CSS3', 'value': 'NYC'},
                                                {'label': 'JS', 'value': 'NYC'},
                                                {'label': 'JQuery', 'value': 'NYC'},
                                                {'label': 'ReactJS', 'value': 'NYC'},
                                                {'label': 'NodeJS', 'value': 'NYC'},
                                                {'label': 'PHP', 'value': 'NYC'},
                                                {'label': 'MySQL / Oracle / PostgreSQL', 'value': 'NYC'},
                                                {'label': 'MongoDB / Hadoop', 'value': 'NYC'},
                                                {'label': 'Python', 'value': 'NYC'},
                                                {'label': 'Basic / Shell', 'value': 'MTL'},
                                                {'label': 'C / C++', 'value': 'SF'},
                                                {'label': 'Ruby on Rails', 'value': 'SF'},
                                                {'label': 'Ada', 'value': 'SF'},
                                                {'label': 'Swift', 'value': 'SF'},
                                                {'label': 'Java', 'value': 'SF'},
                                                {'label': 'Microsoft Office', 'value': 'SF'},
                                                {'label': 'Git', 'value': 'SF'},
                                                {'label': 'Électronique', 'value': 'SF'}

                                        ],
                                        value="MYC",
                                        multi=True,
                                        id="domainesPredilectionPostuler"
                                        ),


                                        html.P(
                                                "Parlez - nous de vos expériences professionnelles :",
                                                style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "14",
                                                }
                                              ),
                                        dcc.Textarea(
                                                placeholder='Parlez - nous de vous !',
                                                style={'width': '100%'},
                                                id="experiencesPostuler"
                                                ),


                                        html.P(
                                                "Lien de votre repo GitHub, GitLab, etc ... :",
                                                style={
                                                "float": "left",
                                                "marginTop": "14",
                                                "marginBottom": "2",
                                                },
                                                className="row"
                                              ),
                                        dcc.Input(
                                                id="repoPostuler",
                                                placeholder="Entrez une URL ...",
                                                type="text",
                                                value="",
                                                style={"width": "100%"},
                                                ),




                                        html.Div(
                                                [
                                                html.Span(
                                                    "3. Test de personnalité",
                                                    style={
                                                    "color": "#506784",
                                                    "fontWeight": "bold",
                                                    "fontSize": "20",
                                                    }
                                                    )],
                                                className="row",
                                                style={"borderBottom": "1px solid #C8D4E3", "marginTop":"75"},
                                                ),


                                                html.P(
                                                        "Auto-évaluez votre niveau :",
                                                        style={
                                                        "textAlign": "left",
                                                        "marginBottom": "2",
                                                        "marginTop": "14",
                                                        },
                                                      ),
                                                dcc.Slider(
                                                        min=1,
                                                        max=5,
                                                        marks={0:"Débutant", 1:"Initié", 2:"Confirmé", 3:"Avancé", 4:"Génie universel"},
                                                        value=0,
                                                        id="niveauPostuler"
                                                        ),


                                                html.P(
                                                        "Vous préférez :",
                                                        style={
                                                        "textAlign": "left",
                                                        "marginBottom": "2",
                                                        "marginTop": "34",
                                                        },
                                                      ),
                                                dcc.Dropdown(
                                                        options=[
                                                        {'label': 'Apple', 'value': 'apple'},
                                                        {'label': 'iMac', 'value': 'iMac'},
                                                        {'label': 'Steve Jobs', 'value': 'steveJobs'}
                                                        ],
                                                        value='MTL'
                                                        ),


                                                html.P(
                                                        "Plus sérieusement. À qui Apple doit son succès mondial ?",
                                                        style={
                                                        "textAlign": "left",
                                                        "marginBottom": "2",
                                                        "marginTop": "34",
                                                        },
                                                      ),
                                                dcc.Dropdown(
                                                        options=[
                                                        {'label': 'Steve Wozniak', 'value': 'steveWozniak'},
                                                        {'label': 'Steve Jobs', 'value': 'steveJobs'}
                                                        ],
                                                        value='MTL',
                                                        id="applePostuler"
                                                        ),






                                                html.Div(
                                                        html.Span(
                                                            "4. Projet",
                                                            style={
                                                            "color": "#506784",
                                                            "fontWeight": "bold",
                                                            "fontSize": "20",
                                                            }
                                                            ),
                                                        className="row",
                                                        style={"borderBottom": "1px solid #C8D4E3", "marginTop":"75"},
                                                        ),


                                                        html.P(
                                                                "Veuillez uploader votre projet au format assignment1.py, assignment2.py, etc ... :",
                                                                style={
                                                                "textAlign": "left",
                                                                "marginBottom": "2",
                                                                "marginTop": "14",
                                                                },
                                                              ),

                                                        dcc.Upload(
                                                                id='fichierPostuler',
                                                                children=html.Div([
                                                                    'Glissez - déposez ou ',
                                                                    html.A('sélectionnez des fichiers')
                                                                ]),
                                                                style={
                                                                'width': '100%',
                                                                'height': '60px',
                                                                'lineHeight': '60px',
                                                                'borderWidth': '1px',
                                                                'borderStyle': 'dashed',
                                                                'borderRadius': '5px',
                                                                'textAlign': 'center',
                                                                'margin': '10px'
                                                                },
                                                                multiple=True
                                                                ),


                                                        html.P(
                                                                "Veuillez uploader les tests de votre projet au format test_assignment1.py, test_assignment2.py, etc ... :",
                                                                style={
                                                                "textAlign": "left",
                                                                "marginBottom": "2",
                                                                "marginTop": "34",
                                                                },
                                                              ),
                                                        dcc.Upload(
                                                                id='testPostuler',
                                                                children=html.Div([
                                                                    'Glissez - déposez ou ',
                                                                    html.A('sélectionnez des fichiers')
                                                                ]),
                                                                style={
                                                                'width': '100%',
                                                                'height': '60px',
                                                                'lineHeight': '60px',
                                                                'borderWidth': '1px',
                                                                'borderStyle': 'dashed',
                                                                'borderRadius': '5px',
                                                                'textAlign': 'center',
                                                                'margin': '10px'
                                                                },
                                                                multiple=True
                                                                )


                            ],
                            className="row",
                            style={"padding": "2% 8%"},
                        ),

                        html.Button(
                                    "Postuler",
                                    id="postuler",
                                    n_clicks=0,
                                    className="button button--primary add"
                                    ),
                        html.Div([], id="zorimar", style={"display":"none"})
                    ],
                    className="modal-content",
                    style={"textAlign": "center"},
                )
            ],
            className="modal",
        ),
        id="candidature",
        style={"display": "none"},
    )



layout = html.Div([
    html.Div([
        html.Div([
                    html.H6('Doctolib - Candidature',
                            className="gs-header gs-text-header padded"),

                    html.Br([]),

                    html.P("Nous avons créé Doctolib pour rendre notre système de santé plus humain, efficace et connecté. Nous travaillons avec les professionnels de santé pour créer les cabinets et les hôpitaux du futur et améliorer le parcours de soins des patients. Depuis 5 ans, nous bâtissons une équipe de sport de plusieurs milliers de talents qui partagent les mêmes valeurs humanistes et qui sont heureux de travailler ensemble. Doctolib s’engage à protéger les données de ses utilisateurs, à garantir leur confidentialité et à appliquer les règles déontologiques des professions médicales et paramédicales.\nLes données de santé sont la propriété exclusive des patients et des praticiens qui utilisent Doctolib. Les équipes de Doctolib n’y ont tout simplement pas accès. Les données de santé des utilisateurs de Doctolib sont conservées chez deux hébergeurs bénéficiant de l’agrément « Hébergeur Agréé de Données de Santé » (HADS) délivré par le Ministère de la Santé. Les données de santé des utilisateurs de Doctolib sont chiffrées et sont gérées en plein accord avec les recommandations du Conseil National de l’Ordre des Médecins (CNOM) et des instances ordinales représentant les autres professions de santé. \n Il n’y aucune publicité sur Doctolib, ni à destination des patients, ni à destination des professionnels de santé. Sur Doctolib, les patients ne peuvent pas évaluer publiquement les professionnels de santé. Sur Doctolib, chaque praticien est traité de manière impartiale et en accord avec le code de déontologie des instances ordinales. \n Venez révolutionner le marché de la santé connectée avec nous. Rejoignez Doctolib."),

                ], className="six columns", style={"text-align":"justify", "margin-top":"20px"}),
    html.Button('Déposer ma candidature', id='candidater', n_clicks=0, className="button button--primary add", style={"width" : "600px", "margin-top":"30px", "margin-left":"40px"}),
    html.Img(src="https://about.doctolib.fr/wp-content/uploads/2018/07/home-hs.png", style={"width":"600px", "padding-top":"60px", "margin-left":"40px"})], style={"width":"100%"}),
    html.Div(
        [
            indicator(
                "#00cc96",
                "Praticiens",
                "65 000"
            ),
            indicator(
                "#119DFF",
                "Établissements de santé",
                "1300"
            ),
            indicator(
                "#119DFF",
                "Visites uniques par mois",
                "25 millions"
            )
        ],
        className="row", style={"padding-top":"30px"}
    ),
    modal()
])

