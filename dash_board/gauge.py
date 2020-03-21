import dash
import dash_daq as daq
import dash_html_components as html

app = dash.Dash(__name__)

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
