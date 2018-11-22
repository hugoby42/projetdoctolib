from visualizer.app.panels.__common__ import *
import visualizer.db.access as access

data=access.getData()
table=data
####TABLE
def make_dash_table(table):
    ''' Return a dash definition of an HTML table for a Pandas dataframe '''
    html_table=[]
    for candidat in table:
        html_row=[]
        html_row.append(html.Td([candidat['id']]))
        html_row.append(html.Td([candidat['nom']]))
        html_row.append(html.Td([candidat['prenom']]))
        html_table.append(html.Tr(html_row))
    return html_table
###
def get_id_candidat():
    return (25)
###
layout = html.Div([  # page 1



        html.Div(children = [

            # Row 1
            html.Div([

                html.Div(children = [
                    html.Table(make_dash_table(table)),
                    html.A(
                    )
                ],),

            ], className="row "),
        ], className="subpage")

    ], className="page")
