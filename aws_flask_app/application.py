import pandas as pd
from db_df import get_df 

import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


application = dash.Dash(__name__)
server = application.server


def serve_layout():
    global datesdict, df_absolut, df_p100000
    df, dates, datelist, datesdict, df_absolut, df_p100000, integer_columns, columnlist = get_df()
    
    return html.Div([
        html.H1('Corona Status ', 
        style={'text-align': 'center'}
        ),

        dcc.RadioItems(
            id = 'slct_abs',
            options = [
                {'label': 'Absolut', 'value': 'absolut'},
                {'label': 'Per 100000', 'value': 'per100000'}
                ],
                value = 'absolut'
        ),
        
        dcc.Dropdown(
            id='slct_count',
            options=columnlist,
            multi=False,
            value=columnlist[0]['value'],
            style={'width': '50%'}
        ),

        html.Div(id='output_container2', children=[]),

        html.Br(),

        dcc.Graph(id='Corona-Karte', figure={}),

        dcc.Slider(
            id = 'slider',
            step = None,
            marks = datesdict,
            value = len(datelist) - 1,
            min = len(datelist) - 7,
            max = len(datelist) - 1
        ),

    ])



application.layout = serve_layout


@application.callback(
    [Output(component_id='output_container2', 
        component_property='children'),
     Output(component_id='Corona-Karte', 
        component_property='figure')],
    [Input(component_id='slct_abs', 
        component_property='value'),
     Input(component_id='slider', 
        component_property='value'),
     Input(component_id='slct_count', 
        component_property='value')]
     )


def update_graph(slct_abs, slider, slct_count):
    container1 = f'Following was selected: {datesdict[slider]}'
    container2 = ''#f'Following was selected: {slct_count}'
    if slct_abs == 'absolut':
        df = df_absolut.copy()
    else:
        df = df_p100000.copy()
    df = df[df['Date'] == datesdict[slider]]
    fig = px.choropleth(
        data_frame=df,
        locations='ISO3',
        color=slct_count,
        hover_name='Country',
        color_continuous_scale='Viridis'
    )
    return container2, fig


if __name__ == '__main__':
    application.run_server(debug=True)
