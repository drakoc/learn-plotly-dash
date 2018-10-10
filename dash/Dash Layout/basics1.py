import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Hello Dash!'),
    html.Div('Dash:Web Dashboards with Python'),
    dcc.Graph(id='example',
              figure=dict(data=[dict(x=[1, 2, 3],
                                     y=[4, 1, 2],
                                     type='bar',
                                     name='SF'),
                                dict(x=[1, 2, 3],
                                     y=[2, 4, 2],
                                     type='bar',
                                     name='NYC')],
                          layout=dict(title='BAR PLOTS!')
                          )
              )
])

if __name__ == '__main__':
    app.run_server(port=8053)
