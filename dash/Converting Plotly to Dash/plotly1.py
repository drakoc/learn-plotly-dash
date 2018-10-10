import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np


app = dash.Dash()

#creating random data

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

print(random_x)
print(random_y)

app.layout = html.Div([
    dcc.Graph(
        id='scatterplot',
        figure={
            'data': [
                go.Scatter(
                    x=random_x,
                    y=random_y,
                    mode='markers',
                    marker={
                        'size':12,
                        'color': 'rgb(51,204,153',
                        'symbol': 'pentagon',
                        'line': {
                            'width': 2
                        }
                    }
                )
            ],
            'layout': go.Layout(
                title='My Scatterplot',
                xaxis={
                    'title': 'Some X title'
                },
                yaxis={
                    'title': 'Some Y title',

                },
                hovermode='closest',
                hoverlabel={
                    'bgcolor': 'rgb(255,255,0)'
                }
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(port=8052)
