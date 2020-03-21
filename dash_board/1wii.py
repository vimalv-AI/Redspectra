import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    html.Div(
        className="row",
        children=[
            html.Div(
                className="six columns",
                children=[
                    html.Div(
                        children=dcc.Graph(
                            id='left-graph',
                            style={'width': 650, 'height': 440},

                            figure={
                                'data': [{
                                    'x': [1, 2, 3],
                                    'y': [3, 1, 2],
                                    'type': 'bar'
                                }],
                                'layout': {
                                    'height': 800,
                                    'margin': {
                                        'l': 10, 'b': 20, 't': 0, 'r': 0
                                    }
                                }
                            }
                        )
                    )
                ]
            ),
            html.Div(
                className="six columns",
                children=html.Div([
                    dcc.Graph(
                        id='right-top-graph',
                        style={'width': 650, 'height': 440},
                        figure={
                            'data': [{
                                'x': [1, 2, 3],
                                'y': [3, 1, 2],
                                'type': 'bar'
                            }],
                            'layout': {
                                'height': 400,
                                'margin': {'l': 10, 'b': 20, 't': 0, 'r': 0}
                            }
                        }
                    ),
                    dcc.Graph(
                        id='right-bottom-graph',
                        style={'width': 650, 'height': 440},
                        figure={
                            'data': [{
                                'x': [1, 2, 3],
                                'y': [3, 1, 2],
                                'type': 'bar'
                            }],
                            'layout': {
                                'height': 400,
                                'margin': {'l': 10, 'b': 20, 't': 0, 'r': 0}
                            }
                        }
                    ),

                ])
            )
        ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
