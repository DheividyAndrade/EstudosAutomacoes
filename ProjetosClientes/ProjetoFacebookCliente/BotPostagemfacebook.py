from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random

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
    return driver


# 1 - Navegar ate o site
driver = iniciar_driver()
driver.get('https://www.facebook.com/')
sleep(1)
# Usado para deixar tela completa do navegador.
driver.maximize_window()
sleep(2)

def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)

campo_email = driver.find_element(By.ID, 'email')
digitar_naturalmente('', campo_email) #campo para email
sleep(2)
campo_senha = driver.find_element(By.XPATH, "//input[@type='password']")
sleep(1)
digitar_naturalmente('', campo_senha) #campo para senha
sleep(2)
botao_entrar = driver.find_element(By.NAME, 'login')
botao_entrar.click()
sleep(5)

#Aguardar Usuario fazer reCAPCHER

print('Você tem 1 minuto Para Realizar o >>reCAPCHER<< ')
sleep(60)

# Clicando nos "agora não"
ActionChains(driver).send_keys(Keys.TAB).perform()
sleep(0.5)
ActionChains(driver).send_keys(Keys.TAB).perform()
sleep(0.5)
ActionChains(driver).send_keys(Keys.ENTER).perform()
sleep(2)


# Voltando a Automação
clicar_campo_escrever = driver.find_element(By.XPATH, "//div[@class='x1i10hfl x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou']")
clicar_campo_escrever.click()
sleep(3)

# Escrevendo Post
campo_escrever = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
digitar_naturalmente('Boa noite', campo_escrever)
sleep(3)

campo_escrever.send_keys(Keys.TAB)
sleep(0.3)
campo_escrever.send_keys(Keys.TAB)
sleep(0.3)
campo_escrever.send_keys(Keys.TAB)
sleep(0.3)
campo_escrever.send_keys(Keys.TAB)
sleep(0.3)
campo_escrever.send_keys(Keys.TAB)
sleep(0.3)
campo_escrever.send_keys(Keys.TAB)
sleep(0.3)
campo_escrever.send_keys(Keys.TAB)
sleep(0.3)
campo_escrever.send_keys(Keys.TAB)
sleep(0.3)
campo_escrever.send_keys(Keys.TAB)
sleep(0.3)
campo_escrever.send_keys(Keys.TAB)
sleep(2)
ActionChains(driver).send_keys(Keys.ENTER).perform()
sleep(3)




input('')
driver.close()

