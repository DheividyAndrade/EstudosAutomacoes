import pyautogui
from time import sleep

# Poisção algo - use o mouseInfo
# Fazer algo com essa posição
# usando game de mineração do site: https://www.crazygames.com/game/doge-miner-2 para mizerar automatico ate passar de fase.

# Clicando no Play Now
pyautogui.moveTo(769, 673, duration=2)
pyautogui.click()
# Aguardando carregar game.
sleep(5)
# Clicando Start
pyautogui.moveTo(764, 610, duration=2)
pyautogui.click()
# aguardando carregar
sleep(10)
# Posicionando para clicar
pyautogui.moveTo(577, 538, duration=2)
# Loop para clicar 100x
for i in range(38):
    pyautogui.click()
