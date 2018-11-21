import dash
import dash_html_components as htlm
import dash_core_components as dcc

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = htlm.Div(
    style = {
        'backgroundColor': colors['background']
    },
    children=[
        htlm.H1(
            children = 'Hello Dash',
            style = {
                'textAlign': 'center',
                'color': colors['text']
            }
        ),
        htlm.H2(
            children='What a beautiful day',
            style = {
                'textAlign': 'center',
                'color': colors['text']
            }
        ),
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
            ],
            style = {
                'textAlign': 'center',
                'color': colors['text']
            }
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
            ],
            style = {
                'textAlign': 'center',
                'color': colors['text']
            }
        )


    ]
)


if __name__=='__main__':
    app.run_server(debug=True)
