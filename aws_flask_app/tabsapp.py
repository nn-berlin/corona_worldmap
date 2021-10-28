import pandas as pd
from db_df import get_df 

import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

ext_stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

application = dash.Dash(__name__, external_stylesheets=ext_stylesheet)
server = application.server

application.layout = html.Div([
    dcc.Tabs(id='tabs-input', value='tab-1', children=[
                    dcc.Tab(label='Poland', value='tab-1'),
                    dcc.Tab(label='Germany', value='tab-2')]
            ),
    dcc.Graph(id='tabs-output', figure={})
])

@application.callback(
    Output('tabs-output', 'figure'),
    Input('tabs-input', 'value'))

def render_content(tab):
    if tab == 'tab-1':
        df, dates = get_df()
        dff = df[(df.Country == 'Poland') & (df.kind == 'absolut')]
        ausgabe1 =  px.scatter(dff, x=dff.Date, y=dff['New Confirmed'])
        return ausgabe1
    elif tab == 'tab-2':
        df, dates = get_df()
        dff = df[(df.Country == 'Germany') & (df.kind == 'absolut')]
        ausgabe2 =  px.scatter(dff, x=dff.Date, y=dff['New Confirmed'])
        return ausgabe2


if __name__ == '__main__':
    application.run_server(debug=True)
