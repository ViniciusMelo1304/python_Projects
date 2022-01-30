import pandas as pd
import plotly.express as px

'''IMPORTANTE: Baixar a base de dados e colocar no mesmo diretório do programa .py'''

'''1° Passo: Importar a base de dados'''
tabela = pd.read_csv(
    'telecom_users.csv')

'''2° Passo: Análise inicial dos dados'''
# print(tabela)

'''3° Passo: Tratamento dos dados
    1. Remoção de colunas inúteis'''

# Linha = 0 = 'index'; Coluna = 1 = 'collumns'
tabela = tabela.drop(["Unnamed: 0"], axis=1)
tabela = tabela.drop(["IDCliente"], axis=1)  # Linha = 0; Coluna = 1
# print(tabela)

''' 2. Correção de valores errados'''

tabela["TotalGasto"] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
# print = (tabela.info())

''' 3. Remoção de valores nulos'''

tabela = tabela.dropna(how='all', axis=1)
tabela = tabela.dropna(how='any', axis=0)
# print = (tabela.info())

'''4° Passo: Análise do Churn'''

# print(tabela["Churn"].value_counts(ascending = True))
# print("\n")
print(tabela["Churn"].value_counts(normalize=True, ascending=True).map(
    "{:.2%}".format))  # Mostra que temos 26.57% de Churn

'''5° Passo: Comparação/Plotagem de gráficos (histogramas) para análise de correlação entre os dados e a coluna Churn'''

for coluna in tabela:
    fig = px.histogram(tabela, x=coluna, color="Churn")
    fig.show()

'''6° Passo: Análise dos gráficos e conclusão/elaboração de novas estratégias'''
