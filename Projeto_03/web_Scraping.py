from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

'''1° Passo: Ligar o Webdriver.Chrome e acessar o Google:'''

opcao_Chrome = Options()
opcao_Chrome.add_experimental_option("detach", True)
opcao_Chrome.add_experimental_option("excludeSwitches", ['enable-logging'])
# Configura o Chrome

navegador = webdriver.Chrome(options=opcao_Chrome)
navegador.get(r"https://www.google.com/")

'''2° Passo: Pesquisar as cotações:
    1. Cotação do Dólar:'''

navegador.find_element(
    By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação Dólar")
navegador.find_element(
    By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
cotacao_Dolar = navegador.find_element(
    By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

print(cotacao_Dolar)

''' 2. Cotação do Euro:'''

navegador.find_element(
    By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/input').clear()
navegador.find_element(
    By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/input').send_keys("Cotação Euro")
navegador.find_element(
    By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_Euro = navegador.find_element(
    By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

print(cotacao_Euro)

''' 3. Cotação do Ouro (Atenção para vírgulas e pontos):'''

navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_Ouro = navegador.find_element(
    By.XPATH, '//*[@id="comercial"]').get_attribute("value")
cotacao_Ouro = cotacao_Ouro.replace(",", ".")

print(cotacao_Ouro)

navegador.quit()

'''3° Passo: Importar a base de dados:'''

tabela = pd.read_excel(
    r"C:\Users\Vinicius\Desktop\Aula 3 - Intensivão de Python\Produtos.xlsx")
# print(tabela)

'''4° Passo: Atualizar a base de dados:'''

tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_Euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_Ouro)
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_Dolar)


'''5° Passo: Atualizar cálculos da base de dados:'''

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

# print(tabela)

'''[EXTRA]: Reformatar a base de dados:'''

for coluna in tabela:
    if coluna == "Cotação" or coluna == "Preço de Compra" or coluna == "Preço de Venda":
        tabela[coluna] = tabela[coluna].map("{:,.2f}".format)
tabela["Margem"] = tabela["Margem"].map("{:.2%}".format)
print(tabela)

'''6° Passo: Exportar a base de dados:'''

tabela.to_excel(r"C:\Users\Vinicius\Desktop\Aula 3 - Intensivão de Python\Produtos Novo.xlsx",
                sheet_name="Nova DB", index=False)
