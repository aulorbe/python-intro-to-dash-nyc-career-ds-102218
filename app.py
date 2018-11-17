import dash # importing the dash framework
import dash_core_components as dcc # importing the core components from dash
import dash_html_components as html # importing the html components from dash
from uber_data import data

# creating a new instance of Dash
app = dash.Dash()


app.layout = html.Div(children=[
    html.H1('Hello, this is my first dash app'),
    html.P('Still under construction... :)'),
    dcc.Graph(
        id = "uber_pricing_data",
        figure = {
            'data': data,
            'layout': {
                'title': "Uber Pricing in Brooklyn and Manhattan"
            }
        }
    )
])



# telling our app to start the server if we are running this file
if __name__ == '__main__':
    app.run_server(debug=True)
