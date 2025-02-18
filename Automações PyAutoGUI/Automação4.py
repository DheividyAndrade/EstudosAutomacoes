# Automação instagram
import pyautogui
from time import sleep

# Clicando em Seguindo
pyautogui.leftClick(795,778, duration=2)
sleep(3)
#Centralizando Mouse
pyautogui.moveTo(473,823, duration=2)
#Loop para rolar scroll 500x
for i in range(500):
    pyautogui.scroll(-1500) #subir
    sleep(3)
  
#Fim
