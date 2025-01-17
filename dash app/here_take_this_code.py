# coding=utf-8
import base64
import dash_daq as daq
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css'])

image_filename = 'logo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
app.title = 'Redspectra'

df = pd.read_csv('https://raw.githubusercontent.com/vimalv-AI/Vimal/master/dash%20app/tmp.csv')

# If you know the name of the column skip this
first_column = df.columns[0]
# Delete first
d1 = df.drop([first_column], axis=1)
d1.to_csv('1_temperature.csv', index=False)
with open('1_temperature.csv', 'r') as f:
    for row in f:
        pass

df1 = pd.read_csv('https://raw.githubusercontent.com/vimalv-AI/Vimal/master/dash%20app/hum.csv')
# If you know the name of the column skip this
first_column = df1.columns[0]
# Delete first
df2 = df1.drop([first_column], axis=1)
df2.to_csv('2_humidity.csv', index=False)
with open('2_humidity.csv', 'r') as f1:
    for row1 in f1:
        pass
df7 = pd.read_csv('https://raw.githubusercontent.com/vimalv-AI/Vimal/master/dash app/temperature.csv')
app.layout = html.Div([
    html.Div([
        html.Img(src='data:image/png;base64,{}'.format(encoded_image), height=45, width=330),
        dcc.Graph(id='example1', style={'width': 1101, 'height': 380, 'overflowX': 'scroll'},
                  figure=px.area(df, x='Time', y='Temperature', title='Live Streaming Temperature Degree °C ',
                                

                  )
    ], className='six columns'
    ),
    html.Div([  # F
        daq.Gauge(
            id='my-gauge',
            style={'width': 1760, 'height': 0},
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
        dcc.Graph(id='example5', style={'width': 1101, 'height': 360, 'overflowX': 'scroll'},
                  figure=px.area(df1, x='Time', y='Relative Humidity', title='Live Streaming Humidity % ', )
                  )
    ], className='six columns'
    ),
    html.Div([
        daq.Gauge(
            id='my-gauge1',
            style={'width': 1760, 'height': 0},
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
]
)

if __name__ == '__main__':
    app.run_server(debug=True)
