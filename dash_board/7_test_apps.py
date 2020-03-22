import pandas as pd
import plotly.express as px

df = pd.read_csv('ph.csv')

fig = px.line(df, x='Date_x', y=',Potential Hydrogen_y', title='PH Values')
fig.show()
