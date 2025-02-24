from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


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
driver.get('https://cursoautomacao.netlify.app/')
sleep(1)
# Usado para deixar tela completa do navegador.
driver.maximize_window()
sleep(1)

# utilizar Scroll ate alertas
driver.execute_script("window.scrollTo(0, 800);")
sleep(2)

# escrever no campo "Digite seu nome
campo_escrever = driver.find_element(By.ID, 'nome')
sleep(1)
campo_escrever.send_keys('Dheividy')
sleep(3)

# Clicar alerta
botao_alerta = driver.find_element(By.ID,'buttonalerta')
sleep(1)
botao_alerta.click()
sleep(1)
# Clicar Ok
alerta1 = driver.switch_to.alert
alerta1.accept()
sleep(2)

# Escrever nome novamente
campo_escrever = driver.find_element(By.ID, 'nome')
sleep(1)
campo_escrever.send_keys('Dheividy')
sleep(3)
# Clicar em Confirmar
botao_confirmar = driver.find_element(By.ID, 'buttonconfirmar')
sleep(1)
botao_confirmar.click()
sleep(1)

# Clicar Ok
alerta2 = driver.switch_to.alert
alerta2.accept()
sleep(2)

# Escrever novamente Nome
campo_escrever = driver.find_element(By.ID, 'nome')
sleep(1)
campo_escrever.send_keys('Dheividy')
sleep(3)
# Clicar Fazer Pergunta
botao_fazer_pergunta = driver.find_element(By.ID, 'botaoPrompt')
sleep(1)
botao_fazer_pergunta.click()
sleep(2)

alerta3 = driver.switch_to.alert
# Responder a pergunta: 'Que dia é hj'?
alerta3.send_keys('Domingo')
sleep(1)
alerta3.accept()
sleep(1)
# Clicar ok Novamente
alerta3.accept()
sleep(2)




input('')
driver.close()

