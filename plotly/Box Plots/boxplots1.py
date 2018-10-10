import plotly.offline as pyo
import plotly.graph_objs as go

y = [1, 14, 14, 15, 16, 18, 18, 19, 19, 20, 20, 23, 24, 26, 27, 27, 28, 29, 33, 54]

data = [go.Box(y=y,
               # display sample values
               boxpoints='all',
               # amount of jitter in the sample points drawn
               jitter=0.5,
               # position of the pounts
               pointpos=-2)]
layout = go.Layout(
    title='Box chart',
    font=dict(
        size=20
    )
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='boxplots1-plot.html')
