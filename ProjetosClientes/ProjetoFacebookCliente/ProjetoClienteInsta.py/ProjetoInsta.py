from selenium import webdriver
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

def logout ():
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    sleep(3)
    botao_perfil = driver.find_element(By.XPATH, "//img[@alt='Foto do perfil de gabrieljlg_']")
    botao_perfil.click()
    sleep(3)
    botao_engrenagem = driver.find_element(By.XPATH, "//div[@class='x6s0dn4 x78zum5 xdt5ytf xl56j7k']")
    botao_engrenagem.click()
    sleep(3)
    botão_sair = driver.find_element(By.XPATH, "//button[@text()='Sair']")
    sleep(3)

# 1 - Navegar ate o site
driver, wait = iniciar_driver()
driver.get('https://www.instagram.com/')
# Usado para deixar tela completa do navegador.
driver.maximize_window()

# Clicar em digitar meu usuario
campo_email_login = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//input[@aria-label='Telefone, nome de usuário ou email']")))
digitar_naturalmente('gabrieljlg_', campo_email_login)
sleep(3)
# Clicar em Digitar minha senha
campo_senha = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
digitar_naturalmente('dheividy789', campo_senha)
sleep(3)
# Clicar no campo entrar
botao_entrar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//div[text()='Entrar']")))
botao_entrar.click()
sleep(15)
# Clicando Esc
ActionChains(driver).send_keys(Keys.ESCAPE).perform()

sleep(2)
while True:
    # Navegar ate a pagina do alvo
    driver.get('https://www.instagram.com/decorartrv/')
    # Clicar na ultima postagem
    ultima_postagem = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//a[@href='/decorartrv/p/DGgaRNiPNqm/']")))
    ultima_postagem.click()
    sleep(3)
    
    while True:
        postagem = wait.until(condicao_esperada.visibility_of_any_elements_located((
            By.XPATH, '//div[@class="_aagw"]')))
        postagem[0].click()
        sleep(5)
        # Verificar se postagem foi curtida, caso não tenha sido, clicar curtir, caso já tenha sido, aguardar 24hrs
        try:
            verifica_curtida = driver.find_element(By.XPATH,
                                                '//section//div[@role="button"]//*[@aria-label="Curtir"]')
        except:
            print('A imagem já havia sido curtida.')
        else:
            botao_curtir = driver.find_elements(By.XPATH,
                                                '//article[@role="presentation"]//section//div[@role="button"]')
            sleep(5)
            driver.execute_script('arguments[0].click()', botao_curtir[0])
            print('Deu certo! A imagem acabou de ser curtida.')
        sleep(86400)




input('')
driver.close()

