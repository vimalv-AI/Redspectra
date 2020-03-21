import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
app.title = 'Redspectra_Dashboard'

app.layout = html.Div([
    html.Div([
        html.Div([
            html.H3('Column 1'),
            dcc.Graph(id='example',

                      figure={'data': [{'x': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                              17, 18, 19, 20, ],
                                        'y': [5, 15, 32, 38, 40, 34, 45, 50, 40, 34, 45, 50, 35, 40,
                                              34, 50, 40, 34, 45, 50,
                                              45, 50, 40, 34, 45, 50, 40, 34, 45, 50],
                                        'type': 'Line', 'name': 'Humidity %'}, ],
                              'layout': {'title': ' Temperature °C Analysis',
                                         'xaxis': dict(title='Time Period (hrs)'),
                                         'yaxis': dict(title='Degree_°C')}

                              }

                      )
        ]
        )
    ]
    ),
    html.Div([
        html.H3('Column 2'),
        dcc.Graph(id='example1',

                  figure={'data': [{'x': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                          17, 18, 19, 20, ],
                                    'y': [5, 15, 32, 38, 40, 34, 45, 50, 40, 34, 45, 50, 35, 40,
                                          34, 50, 40, 34, 45, 50,
                                          45, 50, 40, 34, 45, 50, 40, 34, 45, 50],
                                    'type': 'Line', 'name': 'Humidity %'}, ],
                          'layout': {'title': ' Humidity % Analysis',
                                     'xaxis': dict(title='Time Period (hrs)'),
                                     'yaxis': dict(title='Humidity Percentage_%')}

                          }

                  )
    ]
    )
]
)

if __name__ == '__main__':
    app.run_server(debug=True)
