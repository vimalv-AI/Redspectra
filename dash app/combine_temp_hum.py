import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('Temperature.csv')

df1 = pd.read_csv('Humidity.csv')

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Time'], y=df['Temperature'],
                         mode='lines',
                         name='Temperature'))
fig.add_trace(go.Scatter(x=df1['Time'], y=df1['Relative Humidity'],
                         mode='lines+markers',
                         name='Relative Humidity'))

fig.show()