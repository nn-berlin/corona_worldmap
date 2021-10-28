import pandas as pd
from db_df import get_df 

import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

application = dash.Dash(__name__)
server = application.server


def serve_layout():
    df, dates = get_df()
    dropdown_cols = [{'label': s, 'value': s} for s in df.select_dtypes(include='number').columns]
    kind = [{'label': t, 'value': t} for t in [l for l in df['kind'].unique()]]

    return html.Div([
        
        dbc.Row([
            dbc.Col([
                html.H1(
                    'Corona Status '
                    #,style={'text-align': 'center' 
                        #,'backgroundColor': 'lightgreen'}
                )
            ])
        ]),

        dbc.Row([
            dbc.Col([
                dcc.Markdown(
                    '''Data is **updated daily at 11:35 UTC**. 
                    Source of the data is [COVID19API](https://covid19api.com/) 
                    which itself is sourced from 
                    [John Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19).
                    '''
                    #,style={'text-align': 'center' 
                        #,'backgroundColor':'purple'}
                )
            ])
        ]),

        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dcc.Markdown('''
                        Choose:
                        * absolut counts
                        * counts per 100000 inhabitants'''
                        #, style={'backgroundColor':'orange'}
                    )
                ]),
                dbc.Row([
                    dcc.RadioItems(
                        id='radio_absolut_p100k',
                        options=kind,
                        value=kind[0]['value']
                        #, labelStyle={'backgroundColor':'lightblue'}
                    )
                ]
                #, align={'vertical-align': 'flex-end'}
                )
            ]
            #, width={'offset':1, 'size': 5}
            #, align={'horizontal-align': 'stretch'}
            ),

            dbc.Col([
                dbc.Row([
                    dcc.Markdown('''
                        Choose the value to display:  
                        * new: daily counts
                        * total: aggregated counts since beginning of pandemic'''
                        #,style={'backgroundColor':'orange'}
                    )
                ]),
                dbc.Row([
                    
                    dcc.Dropdown(
                        id='dd_confirmed_input',
                        options=dropdown_cols,
                        multi=False,
                        value=dropdown_cols[0]['value']
                        ,style={
                            #'backgroundColor':'lightblue',
                            'width': '80%'}
                    )  
                ]
                #, align={'vertical-align': 'flex-end'}
                )
            ]
            #, width={'offset':1, 'size': 5}
            #, align={'horizontal-align': 'stretch'}
            )
        ]
        , style={'margin':'8%'}
        ),

        dbc.Row([
            dbc.Col([
                html.Div(id='dd_confirmed_output', children=[])
            ])
        ]),

        dbc.Row([
            dbc.Col([
                dcc.Graph(id='worldmap', figure={}
                )
            ])
        ]),

        dbc.Row([
            dbc.Col([
                dcc.Slider(
                    id='slider_dates',
                    step=None,
                    marks=dates,
                    value=len(dates) - 1,
                    min=0,
                    max=len(dates) - 1
                )
            ])
        ])     
    ])


application.layout = serve_layout


@application.callback(
    [Output('dd_confirmed_output', 'children'),
     Output('worldmap', 'figure')],
    [Input('radio_absolut_p100k', 'value'),
     Input('slider_dates', 'value'),
     Input('dd_confirmed_input', 'value')]
     )

def update_graph(radio_absolut_p100k, slider_dates, dd_confirmed_input):
    dd_confirmed_output = ''#f'Following was selected: {slct_count}'
    
    df, dates = get_df()
    dff = df[(df['kind'] == radio_absolut_p100k) & (df['Date'] == dates[slider_dates])]
    fig = px.choropleth(
        data_frame=dff,
        locations='ISO3',
        color=dd_confirmed_input,
        hover_name='Country',
        color_continuous_scale='YlOrRd')

    return dd_confirmed_output, fig


if __name__ == '__main__':
    application.run_server(debug=True)
