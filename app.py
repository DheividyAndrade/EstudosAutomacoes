import threading
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui
import random

# Variável global para controle da execução
executando = False

def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        time.sleep(random.uniform(0.03, 0.1))  # Tempo aleatório entre teclas

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1400,750', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': 'D:\\Storage\\Desktop\\projetos selenium\\downloads',
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[
        NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
    ])
    return driver, wait

def rodar_automacao():
    global executando
    executando = True  # Define que a automação está rodando
    
    driver, wait = iniciar_driver()
    driver.get('https://stake.bet.br/bem-vindo')
    driver.maximize_window()
    time.sleep(3)

    try:
        # Aceitar Cookies
        cookins = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//button[text()='Aceitar cookies']")))
        cookins.click()
        time.sleep(2)

        # Clicar em "Entrar"
        botao_entrar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//button[text()='Entrar']")))
        botao_entrar.click()
        time.sleep(3)

        # Escrever Email/Login
        campo_email = wait.until(condicao_esperada.element_to_be_clickable((By.NAME, 'username')))
        digitar_naturalmente('deividyandrade@hotmail.com', campo_email)
        time.sleep(2)

        # Escrever Senha
        campo_senha = wait.until(condicao_esperada.element_to_be_clickable((By.NAME, 'password')))
        digitar_naturalmente('Ddguit@r321', campo_senha)
        time.sleep(2)

        # Clicar em "Enviar"
        botao_enviar = wait.until(condicao_esperada.element_to_be_clickable(
            (By.XPATH, "//div[@class='StyledLoadingContainer-sc-zuafez vxcJN']")))
        botao_enviar.click()
        time.sleep(5)

        # Confirmar localização
        botao_entendi = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//button[text()='Entendi']")))
        botao_entendi.click()
        time.sleep(3)

        # Pedir permissão para localização
        pyautogui.alert(text='Permita a Localização do site! VOCÊ TEM 10s', title='ALERTA USUARIO DO BOT!', button='OK')
        time.sleep(12)

        # Fechar guia de localização
        botao_fechar_guia = wait.until(condicao_esperada.element_to_be_clickable(
            (By.XPATH, "//span[@class='StyledModalClose-sc-mv2bgq izwmed']")))
        botao_fechar_guia.click()
        time.sleep(5)

        # Acessar Cassino
        botao_casino = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//img[@alt='casino']")))
        botao_casino.click()
        time.sleep(8)

        # Scroll até "Stake Speed Baccarat"
        ActionChains(driver).send_keys(Keys.DOWN * 20).perform()
        time.sleep(3)

        # Acessar o jogo diretamente
        driver.get('https://stake.bet.br/cassino/jogo/stake-speed-baccarat')
        time.sleep(10)

        # Fechar guia de localização novamente
        botao_fechar_guia = wait.until(condicao_esperada.element_to_be_clickable(
            (By.XPATH, "//span[@class='StyledModalClose-sc-mv2bgq izwmed']")))
        botao_fechar_guia.click()
        time.sleep(5)

        # Botões Jogador/Banca/Apostas/Dobra/Dinheiro

        # Analogia do game
        







        # Manter a automação rodando até ser parada
        while executando:
            time.sleep(1)

    except Exception as e:
        print(f"Erro durante a execução: {e}")

    finally:
        driver.quit()
        print("Automação encerrada.")

def iniciar_thread():
    """Inicia a automação em uma thread separada para não travar a interface."""
    global executando
    if not executando:
        thread = threading.Thread(target=rodar_automacao)
        thread.start()

def parar_automacao():
    """Para a execução da automação."""
    global executando
    executando = False
    print("Automação interrompida pelo usuário.")

# Criando a interface gráfica
janela = tk.Tk()
janela.title("BOT AUTOMAÇÃO CASSINO STAKE - Alisson")
janela.geometry("400x300")
janela.configure(bg="#1e1e1e")

# Título na interface
titulo = tk.Label(janela, text="BOT AUTOMAÇÃO CASSINO STAKE", font=("Arial", 14, "bold"), fg="white", bg="#1e1e1e")
titulo.pack(pady=20)

# Botão Play (Iniciar automação)
botao_play = tk.Button(janela, text="▶ Play", font=("Arial", 12, "bold"), fg="white", bg="green", width=10, command=iniciar_thread)
botao_play.pack(pady=10)

# Botão Stop (Parar automação)
botao_stop = tk.Button(janela, text="⏹ Stop", font=("Arial", 12, "bold"), fg="white", bg="red", width=10, command=parar_automacao)
botao_stop.pack(pady=10)

# Rodar a interface gráfica
janela.mainloop()
