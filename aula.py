# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("base_dados/Vendas.xlsx")
opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as Lojas")

# fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Faturamento das lojas'),
    html.H2(children='Gráfico com o faturamento de todos os produtos separado por loja'),

    html.Div(children='''
        Obs: Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
    '''),
    html.Div(id="texto"),

    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista-lojas'),
    dcc.Graph(
        id='grafico-quantidade-vendas'
    )
])

@app.callback(
    Output(component_id='grafico-quantidade-vendas', component_property='figure'),
    Input(component_id='lista-lojas', component_property='value')
)
def update_output(input_value):
    if input_value == "Todas as Lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == input_value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
