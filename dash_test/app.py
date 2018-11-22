from visualizer.app.panels.__common__ import *


data = [
        {
            'values': [10,90],
            'type': 'pie',
        },
    ]


layout=html.Div([
        dcc.Graph(
            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
                    },
                    'legend': {'x': 0, 'y': 1}
                }
            }
        )
    ])
