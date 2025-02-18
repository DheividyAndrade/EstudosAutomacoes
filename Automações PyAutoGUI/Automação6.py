import pyautogui
import pyperclip

# Procurar Bloco de notas Clicando Tecla win
pyautogui.hotkey('win')
# Escrever 'Bloco de notas'
pyautogui.typewrite('bloco de notas')
# clicar no Bloco de Notas
pyautogui.leftClick(207,383, duration=2)
# Escrever no Bloco de notas 'Automação é Incrível!'
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')
        
escrever_frase('Automação é Incrível!')

#fim
