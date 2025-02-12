# Automação senha e login e jogar no bloco
import pyautogui

# Criar uma variavel de e-mail
email = pyautogui.prompt(text='digite seu e-mail', title='dados de login')

#Criar uma variavel de senha
senha = pyautogui.password(text='digite sua senha',title='dados de login',mask='*')

# Rota que o mouse leva ao bloco de notas
pyautogui.click(335,872,duration=1)

pyautogui.typewrite(email)
pyautogui.press('enter')
pyautogui.typewrite(senha)

# fim
