import dash
import dash_core_components as dcc
import dash_html_components as html 

app=dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

app.layout = html.Div(
                    html.Div([
                            html.Div(
                                [
                                html.H1(children="Dash Tutorial 02"),
                                    html.Div("Summary /explanation goes here")

                               ],   className = "row"), 

            html.Div(
                [
                html.Div([
                
                        dcc.Graph(id='graph1',
                             figure={'data':[
                                 {'x':[1,2,3,4],'y':[3,5,7,20],'type':'bar','name':'TPICAP'}
                                             ],
                                     'layout':{
                                         'title':'dash graph',
                                        'xaxis':dict(
                                            title='x-axis',
                                            titlefont=dict(family='Courier New, monospace',size=20)),
                                         'yaxis':dict(
                                         title='y-axis')

                         }
                     
                     
                 }
                 )

               
            ],className= "six.columns"),
    
                html.Div([
                     dcc.Graph(id='graph2',
                             figure={'data':[{'x':[1,2,3,4],'y':[1,5,7,4],'type':'bar','name':'TPICAP'}],
                                     'layout':{
                                         'title':'dash graph',
                                        'xaxis':dict(
                                            title='x-axis',
                                            titlefont=dict(
                                                family='Courier New, monospace',
                                                size=20)),
                                         'yaxis':dict(
                                         title='y-axis')

                                     }
                     
                     
                         }
                 )
                ],className="six.columns")
    
                ],className="row")


    ])

    )


if __name__ == '__main__':
    app.run_server(debug=True,ssl_context='adhoc')
