# Digitando no pyautogui Whatsapp pesq
import pyautogui
from time import sleep
import pyperclip

# Mover mouse para campo de Digitar
pyautogui.moveTo(648, 1057, duration=2)
# Clicar no Campo de Digitar
pyautogui.click()
# Clicar na Pesquisa
pyautogui.leftClick(276, 155, duration=2)
# Digitar Algo
pyautogui.typewrite('Amor')
# Clicar em amor
pyautogui.leftClick(218,238, duration=2)
sleep(1)
# Digitar 'oi'
pyautogui.typewrite('oi')
# Clicar no Botão de Enviar
pyautogui.leftClick(1881,1001, duration=2)

#Fim
