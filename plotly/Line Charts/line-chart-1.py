import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
np.random.seed(56)


# creating random data

x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

# defining chart data

# create trace with markers (dots)

trace0 = go.Scatter(
    x=x_values,
    y=y_values+6,
    mode='markers',
    name='markers'
)

# create trace with lines

trace1 = go.Scatter(
    x=x_values,
    y=y_values,
    mode='lines',
    name='myLines'
)

# create trace with markers & lines

trace2 = go.Scatter(
    x=x_values,
    y=y_values-6,
    mode='lines+markers',
    name='lines & markers'
)

data = [trace0, trace1, trace2]


# defining chart layout

layout = go.Layout(
    title='Line Charts'
)

# defining chart (figure)

fig = go.Figure(data=data, layout=layout)


# drawing chart (figure)

pyo.plot(fig, filename='line-chart-1-plot.html')
