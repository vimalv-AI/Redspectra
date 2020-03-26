# coding=utf-8
import base64
import dash_daq as daq
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css'])

image_filename = 'rsz_screenshot_from_2020-03-22_03-50-45.png'  # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
app.title = 'Redspectra'

with open('1_temperature.csv', 'r') as f:
    for row in f:
        pass
with open('2_humidity.csv', 'r') as f:
    for row1 in f:
        pass
df = pd.read_csv('1_temperature.csv')
df1 = pd.read_csv('2_humidity.csv')
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
            style={'width': 1550, 'height': 550},
            color={"gradient": True,
                   "ranges": {"green": [0, 50], "yellow": [50, 70], "red": [70, 100]}},
            showCurrentValue=True,
            units="Degree °C ",
            value=float(row1),
            label='Humidity Meter',
            max=100,
            min=0,
        ),
    ]

    )
]
)

if __name__ == '__main__':
    app.run_server(debug=True)
