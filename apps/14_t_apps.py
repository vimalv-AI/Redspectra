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

with open('temp.csv', 'r') as f:
    for row in f:
        pass
df = pd.read_csv('temperature.csv')
app.layout = html.Div([  # a
    html.Div([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image), height=34, width=200),
        html.H4(children='Redspectra'),
        dcc.Graph(id='example1', style={'width': 945, 'height': 330, 'overflowX': 'scroll'},
                  figure=px.area(df, y='Temperature', title='Temperature °C ', )

                  )
    ], className='six columns'
    ),

    html.Div([  # F
        daq.Gauge(
            id='my-gauge',
            style={'width': 1550, 'height': 540},
            color={"gradient": True,
                   "ranges": {"green": [0, 25], "yellow": [25, 35], "red": [35, 50]}},
            showCurrentValue=True,
            units="Degree °C ",

            value=float(row),

            label='Temperature Meter',
            max=50,
            min=0,
        )

    ]
    )
], className="row"
)

if __name__ == '__main__':
    app.run_server(debug=True)
