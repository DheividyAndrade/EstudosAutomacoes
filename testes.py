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
from tkinter import messagebox
import tkinter as tk
from tkinter import scrolledtext
import threading
import random



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
def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.uniform(0.03, 0.1))  # Tempo aleatório entre teclas

# 1 - Navegar ate o site
driver, wait = iniciar_driver()
driver.get('https://stake.bet.br/bem-vindo')
sleep(1)
# Usado para deixar tela completa do navegador.
driver.maximize_window()


# Aceitar Cookies
cookins = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//button[text()='Aceitar cookies']")))
cookins.click()
sleep(2)

# Clicar em "Entrar"
botao_entrar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//button[text()='Entrar']")))
botao_entrar.click()
sleep(3)

# Escrever Email/Login
campo_email = wait.until(condicao_esperada.element_to_be_clickable((By.NAME, 'username')))
digitar_naturalmente('deividyandrade@hotmail.com', campo_email)
sleep(2)

# Escrever Senha
campo_senha = wait.until(condicao_esperada.element_to_be_clickable((By.NAME, 'password')))
digitar_naturalmente('Ddguit@r321', campo_senha)
sleep(2)

# Clicar em "Enviar"
botao_enviar = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, "//div[@class='StyledLoadingContainer-sc-zuafez vxcJN']")))
botao_enviar.click()
sleep(5)
# Pedir permissão para localização
pyautogui.alert(text='Permita a Localização do site! VOCÊ TEM 10s', title='ALERTA USUARIO DO BOT!', button='OK')
sleep(12)

# Fechar guia de localização
botao_fechar_guia = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, "//span[@class='StyledModalClose-sc-mv2bgq izwmed']")))
botao_fechar_guia.click()
sleep(5)

driver.get('https://stake.bet.br/cassino/jogo/stake-speed-baccarat')
sleep(30)

# Fechar guia de localização
botao_fechar_guia = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//span[@class='StyledModalClose-sc-mv2bgq izwmed']")))
botao_fechar_guia.click()

# Centralizando
pyautogui.click(687,212, duration=2)
pyautogui.press('down')
sleep(5)


# Fechando nots
pyautogui.click(825,562,duration=1)
sleep(1)
pyautogui.click(595,245)
sleep(3)


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
        sleep(50)
        aposta()
        sleep(0.5)
        jogador()
        sleep(15)                                 #verde     ou  #vermelha
        if pyautogui.pixelMatchesColor(338, 760,(40, 190, 103) or (243, 61, 61)):
            print('Achamos outra cor que não foi a valida na 4º posição. DOBRANDO!')
            aposta()
            sleep(0.5)
            aposta()
            sleep(0.5)
            jogador()
        else:
            print('Acerto no 4ª posição AZUL!')
            sleep(71)
    elif cor_vermelha_em_posicao(x, 703):
        print(f"Achamos a cor vermelha na posição ({x}, 703), apostando na Banca!")
        sleep(50)
        aposta()
        sleep(0.5)
        banca()
        sleep(15)                               #verde     ou   azul
        if pyautogui.pixelMatchesColor(338, 760,(40, 190, 103) or (62, 138, 238)):
            print("Achamos outra cor que não foi a valida na 4º posição. DOBRANDO!")
            aposta()
            sleep(0.5)
            aposta()
            sleep(0.5)
            banca()
        else:
            print('Acerto na 4ª posição VERMELHA!')
            sleep(71)
    elif cor_verde_em_posicao(x, 703):
        print(f"A cor verde foi encontrada na posição ({x}, 703), passando para a próxima posição sem ação.")
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
'''



# Funções de clique para apostas
def jogador():
    pyautogui.click(801, 730, duration=1)

def banca():
    pyautogui.click(1016, 724, duration=1)

def empate():
    pyautogui.click(908, 717, duration=1)

def aposta():
    pyautogui.click(778, 843, duration=1)

# Funções para identificar cores
def cor_vermelha_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (243, 61, 61))

def cor_azul_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (62, 138, 238))

def cor_verde_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (40, 190, 103))

def cor_branca_em_posicao(x, y):
    return pyautogui.pixelMatchesColor(x, y, (240, 240, 240))

# Funções para verificar as posições específicas
def cor_na_posicao_4():
    return pyautogui.pixelMatchesColor(338, 760, (243, 61, 61))

def cor_na_posicao_4_branca():
    return pyautogui.pixelMatchesColor(338, 760, (240, 240, 240))

def cor_na_posicao_4_azul():
    return pyautogui.pixelMatchesColor(338, 760, (62, 138, 238))

# Função de alerta
def exibir_alerta():
    pyautogui.alert(
        text="**Aguarde até o Gráfico Resetar!**\n\n**Após isso, clique no botão 'Ok' para continuar a automação.**",
        title="**ALERTA**",
        button="**Ok**",
    )

# Variáveis
x = 339
contador = 0

exibir_alerta()  # Exibe o alerta inicial

# Loop principal
while not keyboard.is_pressed('1'):
    if cor_azul_em_posicao(x, 703):
        print(f"Achamos a cor azul na posição ({x}, 703), apostando no Jogador!")
        sleep(47)
        aposta()
        sleep(0.5)
        jogador()
        sleep(15)  # Espera para verificar a 4ª posição
        
        # Verificando a 4ª posição com incremento no X a cada interação
        if cor_azul_em_posicao == pyautogui.pixelMatchesColor(338 + x, 760,(62, 138, 238)):
            print("Achamos a Cor azul na posição 4!")
            sleep(71)
        else:
            sleep(13)
            print('Não foi a cor correspondente. Dobrando Aposta..')
            aposta()
            sleep(0.5)
            aposta()
            sleep(0.5)
            jogador()
            sleep(71)

    elif cor_vermelha_em_posicao(x, 703):
        print(f"Achamos a cor vermelha na posição ({x}, 703), apostando na Banca!")
        sleep(47)
        aposta()
        sleep(0.5)
        banca()
        sleep(15)  # Espera para verificar a 4ª posição
        # Verificando a 4ª posição com incremento no X a cada interação
        if cor_vermelha_em_posicao == pyautogui.pixelMatchesColor(338 + x, 760,(243, 61, 61)):
            print("Achamos a Cor vermelha na posição 4!")
            sleep(71)
        else:
            sleep(13)
            print('Não foi a cor correspondente. Dobrando Aposta..')
            aposta()
            sleep(0.5)
            aposta()
            sleep(0.5)
            banca()
            sleep(71)
            
    elif cor_verde_em_posicao(x, 703):
        print(f"A cor verde foi encontrada na posição ({x}, 703), passando para a próxima posição sem ação.")
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


input('')
driver.close()
