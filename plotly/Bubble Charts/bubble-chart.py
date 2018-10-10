import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df = pd.read_csv('mpg.csv')
print(df.head())

data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg'],
                   # display value when hoovering over
                   text=df['name'],
                   mode='markers',
                   # setting the marker size & displaying the scale
                   marker=dict(size=3 * df['cylinders'],
                               color=df['cylinders'],
                               showscale=True))]
layout = go.Layout(title='Bubble Chart', hovermode='closest')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble-chart-plot')
