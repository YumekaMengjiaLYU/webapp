# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Div([
    # header and intro paragraph
    html.H1('Prediction Tool for Opiod Substance Abuse Treatments'),
    html.Label("Input the patient's data and click on Submit to get the prediction result.")],
    style = {'padding' : '50px' ,
             'backgroundColor' : '#E6E6FA'}),
    html.Label("What is the patient's gender?"),
    dcc.RadioItems(
        id = 'gender',
        options=[
            {'label': 'Male', 'value': 'M'},
            {'label': 'Female', 'value': 'F'},
            {'label': 'Other', 'value': 'O'}
        ],
        value='M'
    ),

    html.Label("What is the patient's age?"),
    dcc.Input(id = 'age', type='number', value = 30),

    html.Label("What is the number of week of this visit?(start from 4)"),
    dcc.Input(id = 'week_num', type='number', value = 4),

    html.Label("What is the number of the patient's missing urine test(s)?"),
    dcc.Input(id = 'missing_num', type='number', value = 0),

    html.Label("What is the number of the patient's positive urine test(s)?"),
    dcc.Input(id = 'positive_num', type='number', value = 0),

    html.Label("What is the patient's treatment plan"),
    dcc.Dropdown(
        id = 'treatment',
        options=[
            {'label': 'CTN27_Buprenorphine/Naloxone', 'value': '1'},
            {'label': 'CTN27_Methadone', 'value': '2'},
            {'label': 'CTN51_Buprenorphine/Naloxone', 'value': '3'},
            {'label': 'CTN51_Extended Release Naltrexone', 'value': '4'},
            {'label': 'CTN30', 'value': '5'}
        ],
        value='1'
    ),
    html.Button(children = 'Submit', id='submit-button-state', n_clicks=0),
    html.Div(id='output-state')

], style={'columnCount': 1})
@app.callback(
    Output('output-state', 'children'),
    [Input('submit-button-state', 'n_clicks')],
    [
    State('week_num', 'value'),
    State('positive_num', 'value'),
    State('missing_num', 'value')])
def update_output(n_clicks, week_num, positive_num,missing_num):
    return u'''

        missing urine ratio is "{}",
        and positive urine ratio is "{}"
    '''.format(missing_num/week_num, positive_num/week_num)

if __name__ == '__main__':
    app.run_server(debug=True)
