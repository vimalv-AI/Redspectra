# coding=utf-8
import base64

import dash
import dash_html_components as html
import dash_core_components as dcc



app.layout = html.Div(
                      html.H1(children=[html.H1(" Welcome to DashBoard"),
                                        dcc.Graph(id='example',
                                                  figure={'data': [{'x': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, ],
                                                                    'y': [5, 15, 32, 38, 40, 34, 45, 50, 40, 34, 45,
                                                                          50],
                                                                    'type': 'Line', 'name': 'Humidity %'},
                                                                   {'x': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10],
                                                                    'y': [10, 20, 34, 35, 40, 48, 45, 50, 40, 34, 45,
                                                                          51, 50, 45, 50],
                                                                    'type': 'Line', 'name': 'Temperature °C '},
                                                                   ],
                                                          'layout': {
                                                              'title': 'Data Visualization Temperature °C & Humidity %',
                                                              'xaxis': dict(title='Time Series (hrs)'),
                                                              'yaxis': dict(title='Degree_°C  & Percentage_%')}
                                                          }
                                                  )
                                        ]
                              )

                      )

if __name__ == "__main__":
    app.run_server(debug=True)
