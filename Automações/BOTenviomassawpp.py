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

telefones = [5564992193649, 5582991681996]

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.typewrite(
        'Olá, Gostaria de conhecer mais sobre nossos BOTS e Automações de Sistemas? (Digite sim, se gostaria de participar.)')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)
