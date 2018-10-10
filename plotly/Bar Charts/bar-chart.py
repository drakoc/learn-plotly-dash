import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('2018WinterOlympics.csv')

trace1 = go.Bar(x=df['NOC'],
                y=df['Gold'],
                name='Gold medals',
                marker=dict(color='#FFD700'))
trace2 = go.Bar(x=df['NOC'],
                y=df['Silver'],
                name='Silver medals',
                marker=dict(color='#9EA0A1'))
trace3 = go.Bar(x=df['NOC'],
                y=df['Bronze'],
                name='Bronze medals',
                marker=dict(color='#CD7F32'))

# barmode 'stack' adds up all traces in one bar, differentiating them with colors
layout = go.Layout(title='Medals in 2018 Winter Olympic Games')
fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

pyo.plot(fig, filename='bar-chart-plot.html')
