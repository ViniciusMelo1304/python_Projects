# O programa utiliza das bibliotecas PyAutoGui, Pandas, PyperClip e Time para automatizar EM PRIMEIRO PLANO (atividades em paralelo enquanto o programa roda podem fazê-lo executar de forma errada).

# Documentação da biblioteca pandas: https://pandas.pydata.org/docs/
# Documentação da biblioteca pyautogui: https://pyautogui.readthedocs.io/en/latest/quickstart.html"

import pyperclip
import pyautogui
import time
import pandas as pd

# Email para onde o relatório será enviado:
email_Diretoria = "vinicius.melo1304@gmail.com"

# Local onde o sistema disponibiliza as vendas do mês anterior:
drive_BD = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing"


# Diretório da base de dados baixada:
# diretorio_Download = "C:\Users\Vinicius\Desktop\Vendas - Dez.xlsx"

# Navegador utilizado:
# navegador = "Chrome"


# Plataforma de Emails utilizada pelo usuário:
plataforma_Emails = "https://mail.google.com/mail/u/1/"

pyautogui.PAUSE = 1

# Abrindo o navegador

# pyautogui.press("winleft") # Abre o navegador por meio de uma busca
# pyautogui.write(navegador) # Atualize a variável navegador com a string referente ao nome do navegador utilizado
# pyautogui.press("enter")
pyautogui.hotkey("winleft", "1") # Caso o navegador já esteja fixo na barra de tarefas -> winleft, posição do navegador
time.sleep(3) # Pausa para o navegador iniciar, caso esteja fechado

# Abrindo o site da base de dados

pyautogui.hotkey("ctrl", "t") # Abre uma nova aba
pyperclip.copy(drive_BD) # Copia o link da variável drive_BD onde consta a base de dados
pyautogui.hotkey("ctrl", "v") # Cola o link (Esse procedimento garante que o programa não terá problemas com caracteres especiais)
pyautogui.press("enter")

# Baixando a base de dados

time.sleep(3) # Pausa para que o site abra completamente, ajuste conforme performance do computador
pyautogui.click(x=328, y=256, clicks = 2) # Abre a pasta no Drive
time.sleep(0.5) # Pausa para que o site abra completamente, ajuste conforme performance do computador
pyautogui.click(x=328, y=256, clicks = 1) # Abre a pasta no Drive
time.sleep(0.5) # Pausa para que o site abra completamente, ajuste conforme performance do computador
# pyautogui.click(x=328, y=256, clicks = 1, button = 'RIGHT') # Click com o botão direito
# pyautogui.click(x=382, y=734, clicks = 1) # Downl oad do arquivo
pyautogui.click(x=1715, y=158, clicks = 1)
time.sleep(0.5) # Pausa para que o site abra completamente, ajuste conforme performance do computador
pyautogui.click(x=1489, y=595, clicks = 1)
time.sleep(5) # Pausa para download do arquivo
pyautogui.press("enter")

# Importando a base de dados no Python

tabela = pd.read_excel(r"C:\Users\Vinicius\Desktop\Vendas - Dez.xlsx") # Importa o arquivo para a variável tabela
# print(tabela) # Mostra a variável tabela para descobrir as colunas que serão trabalhadas

# Calcula soma das quantidades vendidas e faturamento do mês

faturamento = tabela["Valor Final"].sum()
qntd_vendida = tabela["Quantidade"].sum()

# Abre o Gmail para envio do e-mail contendo os cálculos

# pyautogui.press("winleft") # Abre o navegador por meio de uma busca
# pyautogui.write(navegador) # Atualize a variável navegador com a string referente ao nome do navegador utilizado
# pyautogui.press("enter")
# pyautogui.hotkey("winleft", "1") # Abre o navegador que está fixo na primeira posição da barra de tarefas
time.sleep(3)
pyautogui.hotkey("ctrl", "t") # Nova aba
pyperclip.copy(plataforma_Emails) # Abre a plataforma de emails
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(3) # Tempo para o site carregar

# Digita o email

time.sleep(3.5)
pyautogui.click(x=79, y=177) # Click em 'Novo Email'
time.sleep(3.5)
pyperclip.copy(email_Diretoria) # Copia o endereço de email para onde o relatório será enviado (armazenado na variável email_Diretoria). Atenção extra para casos onde é necessário enviar para mais de um email.
pyautogui.hotkey("ctrl", "v")
# pyautogui.press("tab") # Confirma o email digitado
pyautogui.press("tab") # Transiciona para o campo 'Assunto'
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab") # Transiciona para o escopo do email
texto = f'''
Bom dia prezados!

Segue Relatório referentes ao Faturamento e Quantidade de Itens vendidos no mês anterior.

No mês passado faturamos R${faturamento:,.2f}.
E vendemos {qntd_vendida} produtos.

Forte abraços,
Vinícius Melo da Silva
(XX) 12345-6789
''' # Copia a mensagem a ser escrita no escopo do e-mail.
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")