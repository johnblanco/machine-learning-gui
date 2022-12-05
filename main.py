import pandas as pd
from dash import Dash, dcc, html, Input, Output
import os

files = os.listdir('./data')

app = Dash(__name__)
app.layout = html.Div([
    html.Label("File"),
    dcc.Dropdown(
        files,
        files[0],
        id='file-dropdown',
        searchable=False,
        clearable=False
    ),
    html.Label("Target column"),
    dcc.Dropdown(
        id='target',
        searchable=False,
        clearable=False
    ),
    html.Label("Features"),
    dcc.Dropdown(
        id='features',
        multi=True,
        searchable=False,
        clearable=False
    ),
    html.Label("Algorithm"),
    dcc.Dropdown(
        ['Logistic Regression'],
        'Logistic Regression',
        id='algo',
        searchable=False,
        clearable=False),
    html.Label(id="model_metrics")
])


@app.callback(
    Output('model_metrics', 'children'),
    Input('target', 'value'),
    Input('features', 'value')

)
def update_model(target, features):
    return f"target={target} features={features}"


@app.callback(
    Output('target', 'options'),
    Output('features', 'options'),
    Output('target', 'value'),
    Input('file-dropdown', 'value')
)
def update_columns(value):
    columns = pd.read_csv(f'./data/{value}').columns
    return [columns, columns, columns[-1]]


if __name__ == '__main__':
    app.run_server(debug=True)
