import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    html.Div(
        [  # Dropdown component

            html.P(html.Label('Dropdown'), style={'fontWeight': 'bold'}),

            dcc.Dropdown(
                id='myDropdown',
                options=[

                    # dropdown options

                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': 'San Francisco', 'value': 'SF'},
                ],

                # default value for dropdown

                value='SF')
        ],
        style={'marginTop': '30'}
    ),

    html.Div(
        [  # Slider component

            html.P(html.Label('Slider'), style={'fontWeight': 'bold'}),

            dcc.Slider(
                min=-10,
                max=10,
                step=0.5,
                value=0,
                marks={i: '{}'.format(i) for i in range(-10, 11)}),
        ],
        style={'marginTop': '30'}
    ),

    html.Div(
        [  # RadioItems component
            html.P(html.Label('Some Radio Items'), style={'fontWeight': 'bold'}),

            dcc.RadioItems(
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': 'San Francisco', 'value': 'SF'},
                ],

                # default value
                value='SF',

                labelStyle={'display': 'inline-block', 'marginRight': 15}
            )
        ],
        style={'marginTop': '50'}
    )
])

if __name__ == '__main__':
    app.run_server()
