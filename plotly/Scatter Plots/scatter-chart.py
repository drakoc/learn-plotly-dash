# creating chart with random data

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

# creating random data

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# defining chart data

data = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',
                   marker=dict(
                       size=12,
                       color='rgb(51,204,102)',
                       symbol='1',
                       line={'width': 2}),
                   )]


# defining chart layout

layout = go.Layout(title='Hello First Plot',
                   xaxis={'title': 'My X Axis'},
                   yaxis=dict(title='My Y Axis'),
                   hovermode='closest')

# defining chart (figure)

fig = go.Figure(data=data, layout=layout)


# drawing chart (figure)

pyo.plot(fig, filename='scatter-chart-plot.html')
