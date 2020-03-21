import dash
import dash_daq as daq
import dash_html_components as html

app = dash.Dash(__name__,external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css'])

app.layout = html.Div([
    daq.Gauge(
        id='my-gauge',
        color={"gradient": True, "ranges": {"green": [0, 20], "yellow": [20, 35], "red": [35, 100]}},
        showCurrentValue=True,
        units="Degree °C ",
        value=31,
        label='Temperature Meter',
        max=100,
        min=0,
    ),
    daq.Thermometer(
        showCurrentValue=True,
        id='my-thermometer',
        value=40,
        label='Temperature Measurement',
        min=0,
        max=100,
        style={
            'margin-middle': '10%'
        }
    ),
    daq.Gauge(
        id='my-gauge1',
        color={"gradient": True, "ranges": {"red": [0, 40], "yellow": [40, 70], "green": [70, 100]}},
        showCurrentValue=True,
        units="Percentage %",
        value=45,
        label='Humidity Meter',
        max=100,
        min=0,
    ),

])


app.run_server(debug=True)

import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(
    __name__,
    external_stylesheets=[
        'https://codepen.io/amyoshino/pen/jzXypZ.css'
    ]
)

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(children='Hello World',
                        className='nine columns'),
                html.Img(
                    src="http://test.fulcrumanalytics.com/wp-content/uploads/2015/10/Fulcrum-logo_840X144.png",
                    className='three columns',
                    style={
                        'height': '15%',
                        'width': '15%',
                        'float': 'right',
                        'position': 'relative',
                        'margin-top': 10,
                    },
                ),
                html.Div(children='''
                        Dash: A web application framework for Python.
                        ''',
                        className='nine columns'
                )
            ], className="row"
        ),

        html.Div(
            [
            html.Div([
                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'title': 'Graph 1',
                            'xaxis' : dict(
                                title='x Axis',
                                titlefont=dict(
                                family='Courier New, monospace',
                                size=20,
                                color='#7f7f7f'
                            )),
                            'yaxis' : dict(
                                title='y Axis',
                                titlefont=dict(
                                family='Helvetica, monospace',
                                size=20,
                                color='#7f7f7f'
                            ))
                        }
                    }
                )
                ], className= 'six columns'
                ),

                html.Div([
                dcc.Graph(
                    id='example-graph-2',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 9, 8], 'type': 'line', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'title': 'Graph 2'
                        }
                    }
                )
                ], className= 'six columns'
                )
            ], className="row"
        )
    ], className='ten columns offset-by-one')
)

if __name__ == '__main__':
    app.run_server(debug=True)


