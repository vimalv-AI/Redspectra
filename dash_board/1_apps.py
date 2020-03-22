# coding=utf-8
import base64
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq

app = dash.Dash(__name__)
image_filename = 'images.jpeg'  # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
app.title = 'Redspectra'

app.layout = html.Div([
    html.Img(src='data:image/png;base64,{}'.format(encoded_image), height=65, width=65),
    html.Div([html.H1(children='Redspectra'),
              dcc.Graph(id='example1',
                        figure={'data': [{'x': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, ],
                                          'y': [5, 15, 32, 38, 40, 34, 45, 50, 40, 34, 45, 50],
                                          'type': 'Line', 'name': 'Humidity %'},
                                         {'x': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10],
                                          'y': [10, 20, 34, 35, 40, 48, 45, 50, 40, 34, 45, 51, 50,
                                                45, 50],
                                          'type': 'Line', 'name': 'Temperature °C '},
                                         ],
                                'layout': {'title': 'Data Visualization Temperature °C & Humidity %',
                                           'xaxis': dict(title='Time Series (hrs)'),
                                           'yaxis': dict(title='Degree_°C  & Percentage_%')}
                                }

                        ),

              daq.LEDDisplay(
                  label="Temperature °C : Humidity %",
                  value="30:34",
                  size=64,
              ),

              dcc.Graph(id='example2',
                        style={'width': 850, 'height': 440, 'overflowX': 'scroll'},
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

                        ),
              daq.Gauge(
                  id='my-gauge',
                  color={"gradient": True,
                         "ranges": {"green": [0, 20], "yellow": [20, 35], "red": [35, 100]}},
                  showCurrentValue=True,
                  units="Degree °C ",
                  value=31,
                  label='Temperature Meter',
                  max=100,
                  min=0,
              ),
              daq.Thermometer(
                  showCurrentValue=True,
                  id='my_thermometer',
                  value=40,
                  label='Temperature Measurement',
                  min=0,
                  max=100,
                  style={
                      'margin-middle': '10%'
                  }
              ),
              dcc.Graph(id='example3',
                        style={'width': 850, 'height': 440, 'overflowX': 'scroll'},
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

                        ),
              daq.Gauge(
                  id='my-gauge1',
                  color={"gradient": True,
                         "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]}},
                  showCurrentValue=True,
                  units="Percentage %",
                  value=45,
                  label='Humidity Meter',
                  max=100,
                  min=0,
              ),
              daq.Thermometer(
                  showCurrentValue=True,
                  id='my_thermometer1',
                  value=40,
                  label='Temperature Measurement',
                  min=0,
                  max=100,
                  style={
                      'margin-middle': '10%'
                  }
              ),

              ]
             )

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
