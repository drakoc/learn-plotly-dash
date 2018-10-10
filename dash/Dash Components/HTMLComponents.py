import dash
import dash_html_components as html

app = dash.Dash()

# style property is dictionary
# properties in 'style' dict. are camelCase
# class is className

app.layout = html.Div(
    ['This is the outermost div!',
     html.Div('This is inner div! ',
              style={'color': 'red', 'border': '1px red solid', 'margin': '5px', 'textAlign': 'left'}),
     html.Div('Another inner div!',
              style={'color': 'blue', 'border': '3px blue solid', 'margin': '10px', 'textAlign': 'right'})
     ],
    style={'font': 'italic bold 20px arial', 'color': 'green', 'border': '5px green solid', 'text-align': 'center'})

if __name__ == '__main__':
    app.run_server()
