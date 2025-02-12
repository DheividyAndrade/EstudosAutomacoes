# Pegando itens e arrastando para outro lugar
import pyautogui

for i in range(4):
    # Mover ate uma corde
    pyautogui.moveTo(458,328, duration=0.5)
    # Clicar e arrastar, Soltar.
    pyautogui.dragTo(590,787,button='left' , duration=0.5)

#FIM
