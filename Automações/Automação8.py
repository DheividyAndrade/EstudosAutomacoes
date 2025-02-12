# Alertar e pedir Informações no Pyautogui

import pyautogui

# Alerta
#pyautogui.alert(text='iniciando sua automação!', title='Automação de Login',button='ok')

# Pedir informação
#email = pyautogui.prompt(text='Digite seu E-mail', title='Informações obrigatorias')
#print(f'você digitou {email}')

resposta = pyautogui.confirm(text='Continuar rodando nossa automação?', title='Confirmação', buttons=['sim','não','cancelar'])
while resposta == 'sim':
    resposta = pyautogui.confirm(text='Continuar rodando nossa automação?', title='Confirmação', buttons=['sim', 'não', 'cancelar'])

if resposta == 'não':
    pyautogui.alert(text='Encerrando Automação..')
else:
    pyautogui.alert(text='Operação Cancelada!')
