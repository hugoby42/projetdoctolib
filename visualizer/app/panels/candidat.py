from visualizer.app.panels.__common__ import *
import visualizer.db.access as access
#le candidat conserné
id_candidat=10
#importer les données du candidat
data=access.getData()
data_candidat=data[id_candidat]

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
var_quality_tot=str(round(var_quality_tot,2))+'%'
###


colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}



###
stat_table=[['Nombre de fichiers',nb_fichier],
       ['Nombre de fonctions',nb_fonctions_tot],
       ['Nombre de commentaires',nb_comment_tot],
       ['Qualité du nom des variables',var_quality_tot],
       ['Nombre de simmilarités avec la db',nb_cheat_tot]]


###TABLES
def make_dash_table(table):
    ''' Return a dash definition of an HTML table for a Pandas dataframe '''
    html_table=[]
    for row in table:
        html_row=[]
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        html_table.append(html.Tr(html_row))
    return table


###
layout = html.Div([  # page 1



        html.Div([


            # Row 3
            html.Div([

                html.Div([
                    html.H6(data_candidat['nom'] + ' ' + data_candidat['prenom'],
                            className="gs-header gs-text-header padded"),

                    html.P("\
                    Date de naissance : " + data_candidat['dateNaissance'] + "\
                    Lieu de naissance : " + data_candidat['lieuNaissance'] + "\
                    Date d'entretien : " + data_candidat['dateEntretien'] + "\
                    Lieu d'entretien : " + data_candidat['lieuEntretien']),

                ], className="six columns"),

                html.Div([
                    html.H6(["Statistiques du candidat"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(stat_table))
                ], className="six columns"),

            ], className="row "),


        ], className="subpage")

    ], className="page")


