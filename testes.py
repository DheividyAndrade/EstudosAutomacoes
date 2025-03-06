from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import keyboard


contador = 1
def iniciar_driver():
    chrome_options = Options()
    '''
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    arguments = ['--lang=pt-BR', '--window-size=1400,750', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Alterar o local padrão de download de arquivos
        'download.default_directory': 'D:\\Storage\\Desktop\\projetos selenium\\downloads',
        # notificar o google chrome sobre essa alteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    # inicializando o webdriver
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait

# 1 - Navegar ate o site
driver, wait = iniciar_driver()
driver.get('https://stake.bet.br/bem-vindo')
sleep(1)
# Usado para deixar tela completa do navegador.
driver.maximize_window()
sleep(30)


driver.get('https://stake.bet.br/cassino/jogo/stake-speed-baccarat')
sleep(30)
pyautogui.click(687,212, duration=2)
pyautogui.press('down')
sleep(10)




# Analogia

'''
# Exibir alerta antes de iniciar o loop
pyautogui.alert(
    text="Clique no botão Ok, apenas quando o gráfico zerar. Espere até lá...",
    title="Atenção",
    button="Ok"
)

# Funções de clique
def jogador():
    pyautogui.click(801, 730, duration=1)

def banca():
    pyautogui.click(1016, 724, duration=1)

def empate():
    pyautogui.click(908, 717, duration=1)

def aposta():
    pyautogui.click(778, 843, duration=1)

# Funções para verificar cores
def cor_vermelha_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (243, 61, 61))

def cor_azul_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (62, 138, 238))

def cor_verde_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (40, 190, 103))

def cor_branca_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (240, 240, 240))

def posição_4 ():
    pyautogui.pixelMatchesColor(338,760())
# Loop de verificação enquanto a tecla "1" não for pressionada
x = 339  # Posição inicial
contador = 0  # Contador para controlar quantas vezes o `x` foi incrementado

while not keyboard.is_pressed('1'):
    if cor_vermelha_em_posicao(x, 703):  # Se for vermelho, aposta na banca
        print(f"Achamos a cor vermelha na posição ({x}, 703), apostando na Banca!")
        sleep(50)
        aposta()
        sleep(0.5)
        banca()  # Clica em banca
        sleep(71)

    elif cor_azul_em_posicao(x, 703):  # Se for azul, aposta no jogador
        print(f"Achamos a cor azul na posição ({x}, 703), apostando no Jogador!")
        sleep(50)
        aposta()
        sleep(0.5)
        jogador()  # Clica em jogador
        sleep(71)

    elif cor_verde_em_posicao(x, 703):  # Se for verde, apenas pula para a próxima posição
        print(f"A cor verde foi encontrada na posição ({x}, 703), passando para a próxima posição sem ação.")
        sleep(135)
    else:
        print(f"Nenhuma cor encontrada na posição ({x}, 703), verificando a próxima posição...")

    # Incrementa o valor de `x` para a próxima posição
    x += 18
    contador += 1

    # Se `x` atingiu 16 iterações, reseta para a posição inicial
    if contador >= 16:
        print("16 iterações completas. Voltando para a posição inicial...")
        x = 339  # Reseta para a posição inicial
        contador = 0  # Reseta o contador

        # Se a posição inicial for branca, esperar até encontrar outra cor
        while cor_branca_em_posicao(x, 703):
            print("A posição inicial está BRANCA. Aguardando até que apareça outra cor...")
            sleep(1)  # Aguarda 1 segundo antes de verificar novamente

        print("A cor mudou! Retornando à verificação normal.")

    sleep(1)  # Aguarda 1 segundo antes da próxima verificação
'''

# Funções de clique
def jogador():
    pyautogui.click(801, 730, duration=1)

def banca():
    pyautogui.click(1016, 724, duration=1)

def empate():
    pyautogui.click(908, 717, duration=1)

def aposta():
    pyautogui.click(778, 843, duration=1)

# Funções para verificar cores
def cor_vermelha_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (243, 61, 61))

def cor_azul_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (62, 138, 238))

def cor_verde_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (40, 190, 103))

def cor_branca_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (240, 240, 240))

# Função para verificar a cor na posição 4
def cor_na_posicao_4():
    return pyautogui.pixelMatchesColor(338, 760, (243, 61, 61))

# Função para verificar se a posição 4 é branca
def cor_na_posicao_4_branca():
    return pyautogui.pixelMatchesColor(338, 760, (240, 240, 240))

# Função para verificar se a posição 4 é azul
def cor_na_posicao_4_azul():
    return pyautogui.pixelMatchesColor(338, 760, (62, 138, 238))

# Alerta inicial
pyautogui.alert(
    text="**Aguarde até o Gráfico Resetar!**\n\n**Apos isso, Clique no Botão 'Ok' para Iniciar a Automação.**",
    title="**ALERTA**",
    button="**Ok**",
    button_color=(40, 190, 103)  # Cor verde para o botão
)

# Loop de verificação enquanto a tecla "1" não for pressionada
x = 339  # Posição inicial
contador = 0  # Contador para controlar quantas vezes o `x` foi incrementado

while not keyboard.is_pressed('1'):
    if cor_azul_em_posicao(x, 703):  # Se for azul, aposta no jogador
        print(f"Achamos a cor azul na posição ({x}, 703), apostando no Jogador!")

        # Verifica se a posição 4 é azul
        if cor_na_posicao_4_azul():
            print("A posição 4 é azul. Seguindo o código normal.")
            sleep(50)
            aposta()
            sleep(0.5)
            jogador()  # Clica em jogador
        else:
            # Se a cor da posição 4 for branca, aguarda até que mude
            while cor_na_posicao_4_branca():
                print("A posição 4 está BRANCA. Aguardando até que a cor mude...")
                sleep(1)  # Aguarda 1 segundo antes de verificar novamente

            # Após a cor da posição 4 mudar, verifica a cor:
            if cor_na_posicao_4_azul():
                print("A posição 4 agora é azul. Seguindo o código normal.")
                sleep(50)
                aposta()
                sleep(0.5)
                jogador()  # Clica em jogador
            elif cor_na_posicao_4():
                print("A posição 4 agora é vermelha. Realizando aposta 2x e jogador.")
                sleep(50)
                aposta()
                sleep(0.5)
                aposta()  # Realiza aposta 2x
                sleep(0.5)
                jogador()  # Clica em jogador
        
        sleep(71)

    elif cor_vermelha_em_posicao(x, 703):  # Se for vermelho, aposta na banca
        print(f"Achamos a cor vermelha na posição ({x}, 703), apostando na Banca!")

        # Verifica se a posição 4 é vermelha
        if cor_na_posicao_4():
            print("A posição 4 é vermelha. Seguindo o código normal.")
            sleep(50)
            aposta()
            sleep(0.5)
            banca()  # Clica em banca
        else:
            # Se a cor da posição 4 for branca, aguarda até que mude
            while cor_na_posicao_4_branca():
                print("A posição 4 está BRANCA. Aguardando até que a cor mude...")
                sleep(1)  # Aguarda 1 segundo antes de verificar novamente
            
            # Após a cor da posição 4 mudar, verifica a cor:
            if cor_na_posicao_4():
                print("A posição 4 agora é vermelha. Seguindo o código normal.")
                sleep(50)
                aposta()
                sleep(0.5)
                banca()  # Clica em banca
            elif cor_na_posicao_4_azul():
                print("A posição 4 agora é azul. Realizando aposta 2x e banca.")
                sleep(50)
                aposta()
                sleep(0.5)
                aposta()  # Realiza aposta 2x
                sleep(0.5)
                banca()  # Clica em banca
        
        sleep(71)

    elif cor_verde_em_posicao(x, 703):  # Se for verde, apenas pula para a próxima posição
        print(f"A cor verde foi encontrada na posição ({x}, 703), passando para a próxima posição sem ação.")
        sleep(135)
    else:
        print(f"Nenhuma cor encontrada na posição ({x}, 703), verificando a próxima posição...")

    # Incrementa o valor de `x` para a próxima posição
    x += 18
    contador += 1

    # Se `x` atingiu 16 iterações, reseta para a posição inicial
    if contador >= 16:
        print("16 iterações completas. Voltando para a posição inicial...")
        x = 339  # Reseta para a posição inicial
        contador = 0  # Reseta o contador

        # Se a posição inicial for branca, esperar até encontrar outra cor
        while cor_branca_em_posicao(x, 703):
            print("A posição inicial está BRANCA. Aguardando até que apareça outra cor...")
            sleep(1)  # Aguarda 1 segundo antes de verificar novamente

        print("A cor mudou! Retornando à verificação normal.")

    sleep(1)  # Aguarda 1 segundo antes da próxima verificação




input('')
driver.close()
