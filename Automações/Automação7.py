# Executando o MouseInfo 
import pyautogui
from time import sleep

# Clicar na Tecla Win
pyautogui.hotkey('win')
# Digitar "CMD"
pyautogui.typewrite('cmd')
# Presionar 'ENTER'
pyautogui.press('enter')
sleep(1)
# Digitar 'python'
pyautogui.typewrite('python')
pyautogui.press('enter')
sleep(1)
# Digitar 'from mouseinfo import mouseInfo'
pyautogui.typewrite('from mouseinfo import mouseInfo')
pyautogui.press('enter')
sleep(1)
# Digitar 'mouseInfo()'
pyautogui.typewrite('mouseInfo()')
pyautogui.press('enter')

#fim
