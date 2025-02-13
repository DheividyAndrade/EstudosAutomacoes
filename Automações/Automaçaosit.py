import webbrowser
import pyautogui
from time import sleep

# DESAFIO 🥇
# 1) Navegue até o site https://cursoautomacao.netlify.app/
webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(1)
# Centralizar Mouse
pyautogui.click(941, 313, duration=2)
# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
pyautogui.scroll(-850)
sleep(0.5)
pyautogui.click(1470, 499, duration=1)
pyautogui.typewrite('DHEIVIDY')
sleep(0.1)
# 3) Clique em alerta, para gerar a alerta
pyautogui.click(1480, 544, duration=1)
# 4) Feche a alerta
pyautogui.click(1177, 208, duration=1)
# 5) Suba a página totalmente para cima
pyautogui.scroll(850)
sleep(1)
# 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
pyautogui.scroll(-1800)
sleep(1)
pyautogui.click(344,431, duration=1)
sleep(2)
# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
pyautogui.alert(text='VOCÊ TERMINOU',title='ALERTA!', button='OK')

#FIM
