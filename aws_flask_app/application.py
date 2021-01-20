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
    df, dates = get_df()
    dropdown_cols = [{'label': s, 'value': s} for s in df.select_dtypes(include='number').columns]
    kind = [{'label': t, 'value': t} for t in [l for l in df['kind'].unique()]]
    
    return html.Div([
        
        html.H1('Corona Status ', 
        style={'text-align': 'center'}),

        # Input1
        dcc.RadioItems(
            id = 'radio_absolut_p100k',
            options = kind,
            value = kind[0]['value']),
        
        # Input 2
        dcc.Dropdown(
            id='confirmed_input',
            options=dropdown_cols,
            multi=False,
            value=dropdown_cols[0]['value'],
            style={'width': '50%'}),

        # Output 1
        html.Div(id='confirmed_output', children=[]),

        html.Br(),

        # Output 2
        dcc.Graph(id='worldmap', figure={}),

        # Input 3
        dcc.Slider(
            id = 'slider_dates',
            step = None,
            marks = dates,
            value = len(dates) - 1,
            min = 0,
            max = len(dates) - 1),
    ])


application.layout = serve_layout


@application.callback(
    [Output(component_id='confirmed_output', 
        component_property='children'),
     Output(component_id='worldmap', 
        component_property='figure')],
    [Input(component_id='radio_absolut_p100k', 
        component_property='value'),
     Input(component_id='slider_dates', 
        component_property='value'),
     Input(component_id='confirmed_input', 
        component_property='value')]
     )


def update_graph(radio_absolut_p100k, slider_dates, confirmed_input):
    df, dates = get_df()
    
    confirmed_output = ''#f'Following was selected: {slct_count}'
    
    df = df[(df['kind'] == radio_absolut_p100k) & (df['Date'] == dates[slider_dates])]
    
    fig = px.choropleth(
        data_frame=df,
        locations='ISO3',
        color=confirmed_input,
        hover_name='Country',
        color_continuous_scale='YlOrRd'
    )
    return confirmed_output, fig


if __name__ == '__main__':
    application.run_server(debug=True)