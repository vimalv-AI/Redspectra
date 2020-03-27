import datetime

# coding=utf-8
import dash
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/amyoshino/pen/jzXypZ.css'])
html.Div([html.Div([
    html.H1(datetime.datetime.now().strftime('%Y-%m-%d'), style={'opacity': '1', 'color': 'white', 'fontSize': 12}),
    html.H1(datetime.datetime.now().strftime('%H:%M:%S'),
            style={'opacity': '1', 'color': 'white', 'fontSize': 12}),
]
),

    html.Br([

    ]
    )
]
)

if __name__ == '__main__':
    app.run_server(debug=True)
