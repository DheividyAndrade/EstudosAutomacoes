from selenium import webdriver
import webbrowser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import pyautogui


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
        sleep(random.randint(1, 5)/30)


# 1 - Navegar ate o site
driver, wait = iniciar_driver()
driver.get('https://stake.bet.br/bem-vindo')
# Usado para deixar tela completa do navegador.
driver.maximize_window()
sleep(3)

# Aceitar Cookins
cookins = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, "//button[text()='Aceitar cookies']")))
sleep(1)
cookins.click()
sleep(2)
# Clicando no botao entrar
botao_entrar = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, "//button[text()='Entrar']")))
sleep(1)
botao_entrar.click()
sleep(3)

# Escrevendo Email/login
campo_escrever_email = wait.until(
    condicao_esperada.element_to_be_clickable((By.NAME, 'username')))
sleep(1)
digitar_naturalmente('deividyandrade@hotmail.com', campo_escrever_email)
sleep(2)

# Escrevendo senha
campo_escrever_senha = wait.until(
    condicao_esperada.element_to_be_clickable((By.NAME, 'password')))
sleep(1)
digitar_naturalmente('Ddguit@r321', campo_escrever_senha)
sleep(2)

# Botão Enviar
botao_enviar = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, "//div[@class='StyledLoadingContainer-sc-zuafez vxcJN']")))
sleep(1)
botao_enviar.click()
sleep(5)

# Entendi Localização
botao_entendi = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, "//button[text()='Entendi']")))
sleep(1)
botao_entendi.click()
sleep(3)

# Alerta Pedir para Permitir localização
pyautogui.alert(text='Permita a Localização do site! VOCÊ TEM 10s',title='ALERTA USUARIO DO BOT!', button='OK')
sleep(12)

# Fechando Guia de Localização
botao_fechar_guia = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, "//span[@class='StyledModalClose-sc-mv2bgq izwmed']")))
sleep(1)
botao_fechar_guia.click()
sleep(5)

# Clicando casino
botao_casino = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//img[@alt='casino']")))
sleep(1)
botao_casino.click()
sleep(8)

# Usando Scroll para chegar ate o Bakara
driver.execute_script("window.scrollTo(0, 1500);")
sleep(3)




input('')
driver.close()
