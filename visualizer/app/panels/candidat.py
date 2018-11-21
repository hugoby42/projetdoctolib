from visualizer.app.panels.__common__ import *
import visualizer.db.access as access
#le candidat conserné
id_candidat=1
#importer les données du candidat
data=access.getData()
data_candidat=data[id_candidat]
###
def indicator(color, text, id_value, string):
    return html.Div(
        [

            html.P(
                text,
                className="twelve columns indicator_text"
            ),
            html.P(
                id = id_value,
                className="indicator_value"
            ),
            string
        ],
        className="four columns indicator",

    )
###Stats du candidat
fichiers=data_candidat['fichiers']
nb_fichier = len(fichiers)
nb_fonctions_tot = 0
nb_comment_tot = 0
var_quality_tot = 0
nb_cheat_tot = 0
for fichier in fichiers:
    nb_fonctions = fichier['stats']['functionsCount']
    nb_comment = fichier['stats']['commentCount']
    var_quality = fichier['stats']['variableNameQuality']
    nb_cheat = len(fichier['stats']['duplicate'])
    nb_fonctions_tot += nb_fonctions
    nb_comment_tot += nb_comment
    var_quality_tot += var_quality/nb_fichier
    nb_cheat_tot +=nb_cheat
###
layout = html.Div(
    children=[html.H1(children=data_candidat['nom']+' '+data_candidat['prenom']),
    html.Div(
        [
            indicator(
                "#00cc96",
                "Informations personnelles",
                "left_cases_indicator",
                data_candidat['nom']+' '+data_candidat['prenom']+' est né(e) le' + data_candidat['dateNaissance']+' à '+data_candidat['lieuNaissance']+'.'
            ),
            html.P(
                'Stats',
                className="twelve columns indicator_text"
            ),
            html.P(
                id = 'middle_case_indicator',
                className="indicator_value"
            ),
                'Nombre de fichiers : ' + str(nb_fichier) + '\n'
                + 'Nombre de fonctions : ' + str(nb_fonctions_tot) + '\n'
                + 'Nombre de commentaires : ' + str(nb_comment_tot) + '\n'
                + 'Qualité de nom de variable : ' + str(var_quality_tot) + '% \n'
                + 'Nombre de similaritées trouvées : ' + str(nb_cheat_tot) + '\n',


        ],
    ),

        ]
    )
