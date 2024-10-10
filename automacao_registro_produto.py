# Passo 1 - entrar no Chrome
# ° Importa a BIblioteca Pyautogui e time
import pyautogui
from time import sleep

# ° Abrir o Google Chrome
pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
sleep(5)

# ° Entrar no servidor
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
# Passo 2 - fazer login
# ° realizar o login e entrar no site
sleep(5)
pyautogui.click(x=411, y=378)
pyautogui.write('emailexemplo@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha123456')
pyautogui.press('tab')
pyautogui.press('enter')

#  Passo 3 - Importar a base de dados para cadastrar
import pandas as pd

tabela = pd.read_csv("C:\Estudos\Hashtag\Jornada Python\Aula 01 - Python Power Up\Aula 1 - Python PowerUp\produtos.csv")
print(tabela)

# Passo 4 - Cadastrar os Produtos


linha = 0
# Para cada linha da minha tabela
for linha in tabela.index:
    # Selecionar o primeiro campo
    pyautogui.click(x=397, y=258)
    # código
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    # marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    # Tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    # Categoria
    categoria = tabela.loc[linha,'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    # Preço Unitário
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    # Custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    # Obs
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')

    # ° Para apertar enter para cadastrar o produto
    pyautogui.press('enter')
    pyautogui.scroll(5000)


