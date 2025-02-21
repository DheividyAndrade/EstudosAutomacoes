from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

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
sleep(2)
# 2 - encontrar Clicar em Login
botao_login = driver.find_element(By.LINK_TEXT,'Login')
botao_login.click()
sleep(1)
# 3 - encontrar e clicar no campo de email
campo_email = driver.find_element(By.ID,'email')
sleep(1)
# 4 - digitar email
campo_email.send_keys('usuario_dev@hotmail.com')
sleep(1)
# 5 - encontrar e clicar no campo de senha
campo_senha = driver.find_element(By.NAME, 'campoSenha')
sleep(1)
# 6 - digitar senha
campo_senha.send_keys('usuario123')
sleep(1)
# 7 - encontrar e clicar no campo "Enviar"
botao_enviar = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
botao_enviar.click()
sleep(2)


input('')
driver.close()
