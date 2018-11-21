import dash
import dash_html_components as htlm
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = htlm.Div(
    children=[
        htlm.H1('Hello Dash'),
        htlm.H2('What a beautiful day'),
        htlm.Div(
            children =[
                'Je suis un gland',
                htlm.H1('Tu es un gland'),
                dcc.Graph(
                    id = 'Magnifique Graphe',
                    figure = {
                        'data':[
                            {'x':[0,1,2], 'y':[0,1,2], 'type':'lines', 'name': 'Pokemon'}
                        ],
                        'layout':{
                            'title': 'Pikachu'
                        }

                    }
                )
            ]
        ),
        htlm.Div(
            children =[
                'Je suis un gland',
                htlm.H1('Tu es un gland'),
                dcc.Graph(
                    id = 'Magnifique Graphe n°2',
                    figure = {
                        'data':[
                            {'x':[0,1,2], 'y':[0,1,2], 'type':'lines', 'name': 'Pokemon'}
                        ],
                        'layout':{
                            'title': 'Pikachu'
                        }

                    }
                )
            ]
        )


    ]
)


if __name__=='__main__':
    app.run_server(debug=True)
