import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/vimalv-AI/Vimal/master/dash_board/ph.csv')

fig = px.line(df, x='Date_x', y=',Potential Hydrogen_y', title='PH Values')
fig.show()
