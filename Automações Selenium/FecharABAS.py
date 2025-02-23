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


driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')
# Usado para deixar tela completa do navegador.
driver.maximize_window()
sleep(1)
# 1) Salvar nossa janela atual
janela_inicial = driver.current_window_handle
print(f'primeira janela: {janela_inicial}')
# 2) Abrir um nova janela
driver.execute_script('window.scrollTo(0,500);')
sleep(3)
botao_abrir_janela = driver.find_element(
    By.XPATH, "//button[text()='Abrir aba']")
sleep(1)
driver.execute_script('arguments[0].click()', botao_abrir_janela)
sleep(1)
# 3) quais abas estão abertas
abas = driver.window_handles
for aba in abas:
    print(aba)
    if aba not in janela_inicial:
        # alterar para essa nova aba
        driver.switch_to.window(aba)
        sleep(2)
        campo_senha = driver.find_element(By.ID, "senha")
        sleep(2)
        campo_senha.send_keys('123456')
        sleep(2)
        #Fechando a ABA
        driver.close()
driver.switch_to.window(janela_inicial)

input('')
driver.close()