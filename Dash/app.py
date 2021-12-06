from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })
# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

df_police = pd.read_csv('../police_violence_cleaned_again.csv')
df_population = pd.read_csv('../state_population.csv')

fig1 = px.bar(df_police.sort_values(by='state'), x='state', 
                        color='state', 
                        width=500, 
                        labels={'state':'States', 'count':'Count'},
                        color_discrete_sequence=px.colors.qualitative.Bold)
fig2 = px.bar(df_police, x='age')

app.layout = html.Div(children=[

    html.H1(children='Police Firearm Discharge', className='Header'),

    html.Div(children='''Dash: A web application framework for your data.'''),

    dcc.Graph(
        id='example-graph',
        figure=fig1
    ),

    dcc.Graph(
        id='example-graph1',
        figure=fig1
    ),

])



if __name__ == '__main__':
    app.run_server(debug=True)