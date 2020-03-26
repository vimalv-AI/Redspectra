# coding=utf-8
import base64
import dash_daq as daq
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css'])

image_filename = 'Screenshot from 2020-03-25 23-54-55.png'  # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
app.title = 'Redspectra'

df = pd.read_csv('https://raw.githubusercontent.com/vimalv-AI/Vimal/master/apps/1_temperature.csv')
df.to_csv('1_temperature.csv', index=None)
with open('1_temperature.csv', 'r') as f:
    for row in f:
        print(row)

df1 = pd.read_csv('https://raw.githubusercontent.com/vimalv-AI/Vimal/master/apps/2_humidity.csv')
df1.to_csv('2_humidity.csv', index=None)
with open('2_humidity.csv', 'r') as f1:
    for row1 in f1:
        print (row1)
app.layout = html.Div([
    html.Div([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image), height=40, width=255),
        dcc.Graph(id='example1', style={'width': 950, 'height': 330, 'overflowX': 'scroll'},
                  figure=px.area(df, y='Temperature', title='Temperature °C ', )

                  )
    ], className='six columns'
    ),

    html.Div([  # F
        daq.Gauge(
            id='my-gauge',
            style={'width': 1550, 'height': 50},
            color={"gradient": True,
                   "ranges": {"green": [0, 25], "yellow": [25, 35], "red": [35, 50]}},
            showCurrentValue=True,
            units="Degree °C ",

            value=float(row),

            label='Temperature Meter',
            max=50,
            min=0,
        )
    ], className="row"
    ),
    html.Div([
        dcc.Graph(id='example5', style={'width': 950, 'height': 330, 'overflowX': 'scroll'},
                  figure=px.area(df1, y='humidity', title='Humidity % ', )
                  )
    ], className='six columns'
    ),
    html.Div([
        daq.Gauge(
            id='my-gauge1',
            style={'width': 1550, 'height': 50},
            color={"gradient": True,
                   "ranges": {"green": [0, 50], "yellow": [50, 70], "red": [70, 100]}},
            showCurrentValue=True,
            units=" Humidity % ",
            value=float(row1),
            label='Humidity Meter',
            max=100,
            min=0,
        )
    ]
    ),
    dcc.Graph(id='example7', style={'width': 1245, 'height': 365.5, 'overflowX': 'scroll'},
              figure={'data': [{'x': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, ],
                                'y': [5, 15, 32, 38, 40, 34, 45, 50, 40, 34, 45, 50],
                                'type': 'Line', 'name': 'Humidity %'},
                               {'x': [0, 1, 2, 4, 5, 6, 7, 8, 9, 10],
                                'y': [10, 20, 34, 35, 40, 48, 45, 50, 40, 34, 45, 51, 50,
                                      45, 50],
                                'type': 'Line', 'name': 'Temperature °C '},
                               ],
                      'layout': {'title': 'Temperature °C & Humidity %',
                                 'xaxis': dict(title='Time Series (hrs)'),
                                 'yaxis': dict(title='Degree_°C  & Percentage_%')}
                      }

              ),

]
)

if __name__ == '__main__':
    app.run_server(debug=True)
