# Como usar a função click
import pyautogui

# Click personalizado 
pyautogui.click(454,520, clicks=1000, interval=0.1, button='left',duration=2)

# comando para mouseinfo:
# python
# from mouseinfo import mouseInfo 
# mouseInfo()                           

# Comandos pyautogui:
# pyautogui.moveTo(1783,74, duration=2)
# pyautogui.move(50,0,duration=2) <-- para especificar qual eixo quer q mova. (ai esta usando o eixo X).
# pyautogui.click() <-- usado para clicar 

# ex de repetição de click:
for i in range(100):       
  pyautogui.click()   <---  #vai clicar 100x   obs: add a biblioteca time>sleep para dar um tempo entre os clicks.

# pyautogui.click(clicks=2) <-- numeros de clicks(no caso 2 no ex).

# pyautogui.click(button='right') <-- escolhendo botão para clicar( no exemplo botão direito mouse).

# pyautogui.moveTo(duration=2) <-- duração percorrida da movimentação do mouse.

# pyautogui.click(interval=1) <-- usado por ex para dar um intervalo entre clicks.

# pyautogui.doubleclick() <- 2 clicks com mouse.

# pyautogui.rightclick() <- Clica botão direito mouse.

# pyautogui.middleclick() <- Clica botão do meio do mouse.

# pyautogui.tripleclick() <- 3 clicks com mouse.

# pyautogui.dragto() <- Clicar e arrastar

#Simulando Scroll do Mouse
pyautogui.scroll(500) #subir
pyautogui.scroll(-500) #descer

# Digitar Algo
pyautogui.typewrite('Amor') # obs: import pyperclip, todos os acentos vão dar certo.

# pyautogui.hotkey('ctrl' , 'v') <- comando para usar horkeys do teclado.

# pyautigui.press('tab') <- usado para usar botões de atalho do teclado.

# print(pyautogui.KEYBOARD_KEYS) <- PARA VER TODOS AS TECLAS.

# pyautogui.alert(text='iniciando sua automação', title='Automação de Login',button='ok') <- usado para dar alertas ao Usuario.

# Pedir informação 
email = pyautogui.prompt(text='Digite seu E-mail', title='Informações obrigatorias')
print(f'você digitou {email}') <- usado para pedir informações 

#