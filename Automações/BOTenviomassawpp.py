'''QUAIS PASSOS MANUAIS PRECISO FAZER PARA ENVIAR UMA MENSAGEM PARA VARIAS PESSOAS
NO WHATSAPP:

1 - LISTA DE NÚMEROS
2 - ENVIAR INDIVIDUALMENTE UMA MENSAGEM PARA CADA PESSOA
3 - PAUSAR ENTRE CADA ENVIO

PASSOS:
1 - ESCOLHER UM CONTATO
2 - ENVIAR MENSAGEM PARA ESSE CONTATO
        CODIGO FORNECIDO PELO WPP
3 - REPETIR ISSO PARA OUTROS CONTATOS'''

import webbrowser
import pyautogui
from time import sleep
import pyperclip

mensagem = "Olá, Gostaria de conhecer mais sobre nossos BOTS e Automações de Sistemas? (Digite sim, se gostaria de participar.)"

# Forma simples de enviar para contatos em massa 
# telefones = [55xxxxxxxxxx, 55xxxxxxxxxxx]

# enviando para contatos em massa atraves de um arquivo
telefones = []

# forma com arquivo
with open('fones.txt' ,'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0]) 
    print(telefones)

# Loop
for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyperclip.copy(mensagem)  # Copia a mensagem para a área de transferência
    pyautogui.hotkey("ctrl", "v")  # Cola a mensagem no chat
    sleep(5)
    pyautogui.press('enter')
    sleep(300)

# Fim
