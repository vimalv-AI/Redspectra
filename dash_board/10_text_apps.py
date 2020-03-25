# coding=utf-8
import base64
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
import pandas as pd

dt = pd.read_csv('mtt.csv')
dk = dt.tail()
dk1 = dk.T
test_list = [dk1]

for i in range(0, len(test_list)):

    if i == (len(test_list) - 1):
        print (i)
# coding=utf-8


app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css'])

image_filename = 'rsz_screenshot_from_2020-03-22_03-50-45.png'  # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
app.title = 'Redspectra'

app.layout = html.Div([  # b
    html.Div([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image), height=34, width=200),
        # html.H4(children='Redspectra'),
        dcc.Graph(id='example1', style={'width': 1245, 'height': 365.5, 'overflowX': 'scroll',
                                        'background-image': '116942.jpg'},
                  figure={'data': [{'x': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, ],
                                    'y': [5, 15, 32, 38, 40, 34, 45, 50, 40, 34, 45, 50],
                                    'type': 'area', 'name': 'Humidity %'},
                                   {'x': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10],
                                    'y': [10, 20, 34, 35, 40, 48, 45, 50, 40, 34, 45, 51, 50,
                                          45, 50],
                                    'type': 'area', 'name': 'Temperature °C '},
                                   ],
                          'layout': {'title': 'Temperature °C & Humidity %',
                                     'xaxis': dict(title='Time Series (hrs)'),
                                     'yaxis': dict(title='Degree_°C  & Percentage_%')}
                          }

                  ),

        html.Div([  # c
            html.Div([  # d
                dcc.Graph(id='example3',
                          style={'width': 940, 'height': 365.5, 'overflowX': 'scroll',
                                 # 'margin': {'l': 10, 'b': 0,'t': 10, 'r': 0}
                                 },
                          figure={'data': [
                              {'x': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                     21, 22,
                                     23, 24],
                               'y': [34, 45, 50, 40, 34, 5, 15, 32, 38, 40, 34, 45, 50, 40,
                                     45, 50, 40, 34, 45, 50],
                               'type': 'Area', 'name': 'Humidity %'}, ],
                              'layout': {'title': ' Temperature °C Analysis',
                                         'xaxis': dict(title='Time Period (hrs)'),
                                         'yaxis': dict(title='Degree_°C')

                                         }
                          }
                          )
            ], className='six columns'
            ),  # d

            html.Div([  # F
                daq.Gauge(
                    id='my-gauge',
                    style={'width': 1500, 'height': 840, 'margin': {'l': 20, 'b': 0, 't': 0, 'r': 0}},
                    color={"gradient": True,
                           "ranges": {"green": [0, 25], "yellow": [25, 35], "red": [35, 50]}},
                    showCurrentValue=True,
                    units="Degree °C ",
                    value=int(i),
                    label='Temperature Meter',
                    max=50,
                    min=0,
                ),
            ], className='six columns'
            )  # F
        ], className="row"
        ),
        html.Div([
            dcc.Graph(id='example8',
                      style={'width': 1040, 'height': 365.5, 'overflowX': 'scroll',
                             # 'margin': {'l': 10, 'b': 0,'t': 10, 'r': 0}
                             },
                      figure={'data': [
                          {'x': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                 20,
                                 21, 22,
                                 23, 24],
                           'y': [34, 45, 38, 40, 34, 45, 50, 40,
                                 45, 50, 40, 34, 45, 50],
                           'type': 'Line', 'name': 'Humidity %'}, ],
                          'layout': {'title': ' Temperature °C Analysis',
                                     'xaxis': dict(title='Time Period (hrs)'),
                                     'yaxis': dict(title='Degree_°C')

                                     }
                      }
                      )
        ], className='six columns'),  # h
        html.Div([
            daq.Gauge(
                id='my-gauge1',
                style={'width': 1250, 'height': 840},
                color={"gradient": True,
                       "ranges": {"green": [0, 25], "yellow": [25, 35], "red": [35, 50]}},
                showCurrentValue=True,
                units="Degree °C ",
                value=31,
                label='Humidity Meter',
                max=50,
                min=0,
            ),
        ]
            , className='six columns'
        )
    ]
    )

]
    , className="row"
)  # b

if __name__ == '__main__':
    app.run_server(debug=True)
