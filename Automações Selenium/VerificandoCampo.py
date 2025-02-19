from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/desafios.html') # link site para abrir.

botao1 = driver.find_element(By.ID, 'btn1')
botao2 = driver.find_element(By.CLASS_NAME, 'btn2.btn.btn-dark')
botao3 = driver.find_element(By.CLASS_NAME, 'btn2.btn.btn-warning')

if botao1.is_enabled():
    print('Botão 1 Está Abilitado')
else:
    print('Botão 1 está Desabilitado')
if botao2.is_enabled():
    print('Botão 2 está Abilitado')
else:
    print('Botão 2 está Desabilitado')
if botao3.is_enabled():
    print('Botão 3 está Abilitado')
else:
    print('botão 3 está Desabilitado')
    


input('')
driver.close()
