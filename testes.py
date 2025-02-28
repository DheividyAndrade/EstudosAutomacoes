import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
import random
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

# Função para iniciar o driver do Selenium
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
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
    return driver, wait

# Função para digitar texto de forma mais natural
def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)

# Função para executar o bot
def iniciar_bot():
    try:
        driver, wait = iniciar_driver()
        driver.get('https://stake.bet.br/bem-vindo')
        driver.maximize_window()
        sleep(3)

        cookins = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//button[text()='Aceitar cookies']")))            
        sleep(1)
        cookins.click()
        sleep(2)

        botao_entrar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//button[text()='Entrar']")))
        sleep(1)
        botao_entrar.click()
        sleep(3)

        campo_escrever_email = wait.until(condicao_esperada.element_to_be_clickable((By.NAME, 'username')))
        sleep(1)
        digitar_naturalmente('deividyandrade@hotmail.com', campo_escrever_email)
        sleep(2)

        campo_escrever_senha = wait.until(condicao_esperada.element_to_be_clickable((By.NAME, 'password')))
        sleep(1)
        digitar_naturalmente('Ddguit@r321', campo_escrever_senha)
        sleep(2)

        botao_enviar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//div[@class='StyledLoadingContainer-sc-zuafez vxcJN']")))
        sleep(1)
        botao_enviar.click()
        sleep(5)

        botao_entendi = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//button[text()='Entendi']")))
        sleep(1)
        botao_entendi.click()
        sleep(600)

        botao_spam = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//span[@class='StyledModalClose-sc-mv2bgq izwmed']")))
        sleep(2)
        botao_spam.click()
        sleep(5)

        sleep(12)

        botao_menu = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//i[@class='icon-menu'")))
        sleep(1)
        botao_menu.click()
        sleep(2)

        botao_casino = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//img[@alt='casino'")))
        sleep(1)
        botao_casino.click()
        sleep(5)

        driver.execute_script("window.scrollTo(0, 800);")

        sleep(1000)

        driver.close()
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao executar o bot: {e}")

# Função para criar a interface
def criar_interface():
    root = tk.Tk()
    root.title("BOT Casino Alisson")
    root.geometry("400x300")

    label = tk.Label(root, text="Bem-vindo ao BOT Casino Alisson", font=("Arial", 16))
    label.pack(pady=30)

    botao_comecar = tk.Button(root, text="Começar", font=("Arial", 14), command=iniciar_bot)
    botao_comecar.pack(pady=10)

    root.mainloop()

# Chamar a função para iniciar a interface
criar_interface()
