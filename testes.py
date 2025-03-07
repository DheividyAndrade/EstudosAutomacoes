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




'''
# Analogia

def jogador():
    pyautogui.click(801, 730, duration=1)

def banca():
    pyautogui.click(1016, 724, duration=1)

def empate():
    pyautogui.click(908, 717, duration=1)

def aposta():
    pyautogui.click(778, 843, duration=1)

def cor_vermelha_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (243, 61, 61))

def cor_azul_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (62, 138, 238))

def cor_verde_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (40, 190, 103))

def cor_branca_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (240, 240, 240))

def cor_na_posicao_4():
    return pyautogui.pixelMatchesColor(338, 760, (243, 61, 61))

def cor_na_posicao_4_branca():
    return pyautogui.pixelMatchesColor(338, 760, (240, 240, 240))

def cor_na_posicao_4_azul():
    return pyautogui.pixelMatchesColor(338, 760, (62, 138, 238))

def exibir_alerta():
    pyautogui.alert(
        text="**Aguarde até o Gráfico Resetar!**\n\n**Após isso, clique no botão 'Ok' para continuar a automação.**",
        title="**ALERTA**",
        button="**Ok**",
    )

x = 339
contador = 0

exibir_alerta()  # Exibe o alerta inicial

while not keyboard.is_pressed('1'):
    if cor_azul_em_posicao(x, 703):
        print(f"Achamos a cor azul na posição ({x}, 703), apostando no Jogador!")
        if cor_na_posicao_4_azul():
            sleep(50)
            aposta()
            sleep(0.5)
            jogador()
        else:
            while cor_na_posicao_4_branca():
                sleep(1)
            if cor_na_posicao_4_azul():
                sleep(50)
                aposta()
                sleep(0.5)
                jogador()
            elif cor_na_posicao_4():
                sleep(50)
                aposta()
                sleep(0.5)
                aposta()
                sleep(0.5)
                jogador()
        sleep(71)
    elif cor_vermelha_em_posicao(x, 703):
        print(f"Achamos a cor vermelha na posição ({x}, 703), apostando na Banca!")
        if cor_na_posicao_4():
            sleep(50)
            aposta()
            sleep(0.5)
            banca()
        else:
            while cor_na_posicao_4_branca():
                sleep(1)
            if cor_na_posicao_4():
                sleep(50)
                aposta()
                sleep(0.5)
                banca()
            elif cor_na_posicao_4_azul():
                sleep(50)
                aposta()
                sleep(0.5)
                aposta()
                sleep(0.5)
                banca()
        sleep(80)
    elif cor_verde_em_posicao(x, 703):
        print(f"A cor verde foi encontrada na posição ({x}, 703), passando para a próxima posição sem ação.")
        sleep(130)
    else:
        print(f"Nenhuma cor encontrada na posição ({x}, 703), verificando a próxima posição...")
    
    x += 18
    contador += 1
    
    if contador >= 16:
        print("16 iterações completas. Voltando para a posição inicial e exibindo alerta...")
        exibir_alerta()
        x = 339
        contador = 0
        while cor_branca_em_posicao(x, 703):
            sleep(1)
    
    sleep(1)                                  
'''



def jogador():
    pyautogui.click(801, 730, duration=1)

def banca():
    pyautogui.click(1016, 724, duration=1)

def empate():
    pyautogui.click(908, 717, duration=1)

def aposta():
    pyautogui.click(778, 843, duration=1)

def cor_vermelha_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (243, 61, 61))

def cor_azul_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (62, 138, 238))

def cor_verde_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (40, 190, 103))

def cor_branca_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (240, 240, 240))

def cor_na_posicao_4():
    return pyautogui.pixelMatchesColor(338, 760, (243, 61, 61))

def cor_na_posicao_4_branca():
    return pyautogui.pixelMatchesColor(338, 760, (240, 240, 240))

def cor_na_posicao_4_azul():
    return pyautogui.pixelMatchesColor(338, 760, (62, 138, 238))

def exibir_alerta():
    pyautogui.alert(
        text="**Aguarde até o Gráfico Resetar!**\n\n**Após isso, clique no botão 'Ok' para continuar a automação.**",
        title="**ALERTA**",
        button="**Ok**",
    )

x = 339
contador = 0

exibir_alerta()  # Exibe o alerta inicial

while not keyboard.is_pressed('1'):
    while cor_branca_em_posicao(x, 703):
        print(f"A posição ({x}, 703) está branca. Aguardando até aparecer uma cor válida...")
        sleep(1)
    
    if cor_azul_em_posicao(x, 703):
        print(f"Achamos a cor azul na posição ({x}, 703), apostando no Jogador!")
        if cor_na_posicao_4_azul():
            sleep(50)
            aposta()
            sleep(0.5)
            jogador()
        else:
            while cor_na_posicao_4_branca():
                sleep(1)
            if cor_na_posicao_4_azul():
                sleep(50)
                aposta()
                sleep(0.5)
                jogador()
            elif cor_na_posicao_4():
                sleep(50)
                aposta()
                sleep(0.5)
                aposta()
                sleep(0.5)
                jogador()
        sleep(71)
    elif cor_vermelha_em_posicao(x, 703):
        print(f"Achamos a cor vermelha na posição ({x}, 703), apostando na Banca!")
        if cor_na_posicao_4():
            sleep(50)
            aposta()
            sleep(0.5)
            banca()
        else:
            while cor_na_posicao_4_branca():
                sleep(1)
            if cor_na_posicao_4():
                sleep(50)
                aposta()
                sleep(0.5)
                banca()
            elif cor_na_posicao_4_azul():
                sleep(50)
                aposta()
                sleep(0.5)
                aposta()
                sleep(0.5)
                banca()
        sleep(80)
    elif cor_verde_em_posicao(x, 703):
        print(f"A cor verde foi encontrada na posição ({x}, 703), passando para a próxima posição sem ação.")
        sleep(130)
    else:
        print(f"Nenhuma cor encontrada na posição ({x}, 703), verificando a próxima posição...")
    
    x += 18
    contador += 1
    
    if contador >= 16:
        print("16 iterações completas. Voltando para a posição inicial e exibindo alerta...")
        exibir_alerta()
        x = 339
        contador = 0
        while cor_branca_em_posicao(x, 703):
            print("A posição inicial está BRANCA. Aguardando até aparecer outra cor...")
            sleep(1)
    
    sleep(1)


input('')
driver.close()
