from pydoc import importfile
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

'''
Passo a Passo de um Projeto de Ciência de Dados
    - Passo 1: Entendimento do Desafio
    Calcular com base na database quais dos métodos de propaganda (Colunas 'TV', 'Rádio', 'Jornal') retorna mais faturamento (Coluna 'Vendas'); ensinar à uma IA e prever quanto será o faturamento nos próximos meses.
    - Passo 2: Entendimento da Área/Empresa
    A database da empresa mostra os investimentos em milhares de reais e aponta o faturamento em milhões de reais.
    - Passo 3: Extração/Obtenção de Dados   '''
tabela = pd.read_csv(
    r'C:\Users\Vinicius\Desktop\Aula 4 - Intensivão de Python\advertising.csv')
# print(tabela)
''' - Passo 4: Ajuste de Dados (Tratamento/Limpeza) '''
# print(tabela.info()) # Aponta o tipo dos dados e quantos valores não-nulos tem em cada coluna
# Como há 200 valores não-nulos em cada coluna e todas as colunas são formadas por floats, a DB já está tratada/limpa
''' - Passo 5: Análise Exploratória '''
# sns.pairplot(tabela) # Gera gráficos pairplot (dispersão) relacionando todas as quatro colunas entre si
# Gera um gráfico heatwave, mais visual que o de cima
sns.heatmap(tabela.corr(), cmap='Wistia', annot=True, linewidths=1)
# plt.show() # Mostra os gráficos gerados
''' - Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário) '''
'''     1. Definir e criar as variáveis de treino/teste'''
y = tabela["Vendas"]
x = tabela.drop("Vendas", axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(
    x, y, test_size=0.3, random_state=1)

'''     2. Treino da IA:'''
lin_reg = LinearRegression()
lin_reg.fit(x_treino, y_treino)

arv_reg = RandomForestRegressor()
arv_reg.fit(x_treino, y_treino)

'''     3. Teste da IA:'''
teste_preditivo_linear = lin_reg.predict(x_teste)
teste_preditivo_arvore = arv_reg.predict(x_teste)

'''     4. Verificando R² e RSME (Indicadores de confiabilidade/precisão dos modelos testados):'''
r2_lin = metrics.r2_score(y_teste, teste_preditivo_linear)
rsme_lin = np.sqrt(metrics.mean_squared_error(y_teste, teste_preditivo_linear))
print(f'Teste R² da Regressão Linear: {r2_lin}')
print(f'Teste RSME da Regressão Linear: {rsme_lin}')

r2_arv = metrics.r2_score(y_teste, teste_preditivo_arvore)
rsme_arv = np.sqrt(metrics.mean_squared_error(y_teste, teste_preditivo_arvore))
print(f'Teste R² do Método da Árvore de Regressão: {r2_arv}')
print(f'Teste RSME do Método da Árvore de Regressão: {rsme_arv}')

# O teste retorna RSME menor e R² mais próximo de 1 para o método da Árvore de Regressão - assim, esse é o método mais eficiente.

'''     ALTERNATIVA. Comparando os modelos de forma mais direta:
print(metrics.r2_score(y_teste, teste_preditivo_linear))
print(metrics.r2_score(y_teste, teste_preditivo_arvore))
'''

''' - Passo 7: Interpretação de Resultados  '''
'''     1. Criar nova database e plotar gráficos'''
tabela_previstos = pd.DataFrame()
tabela_previstos["Y do Teste"] = y_teste
tabela_previstos["teste_preditivo_linear"] = teste_preditivo_linear
tabela_previstos["Predição - Árvore"] = teste_preditivo_arvore

tabela_previstos = tabela_previstos.reset_index(drop=True)
fig = plt.figure(figsize=(15, 5))
sns.lineplot(data=tabela_previstos)
plt.show()
print(tabela_previstos)

'''     2. Visualização da importância de cada item:'''
importancia_features = pd.DataFrame(
    arv_reg.feature_importances_, x_treino.columns)
plt.figure(figsize=(5, 5))
sns.barplot(x=importancia_features.index, y=importancia_features[0])
plt.show()
print(tabela[["Radio", "Jornal"]].sum())

''' Passo 8: Deploy e verificação com a planilha dos próximos resultados'''
novos_produtos = pd.read_csv(
    r'C:\Users\Vinicius\Desktop\Aula 4 - Intensivão de Python\novos.csv')

previsao = arv_reg.predict(novos_produtos)
print(previsao)
