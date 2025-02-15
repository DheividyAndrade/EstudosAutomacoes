import pyautogui
from time import sleep
import webbrowser


def logout():
    #clicando fora
    pyautogui.click(1757,133, duration=1)
    sleep(1)
    pyautogui.click(1826, 1004, duration=2)
    sleep(1)
    pyautogui.click(1449, 263, duration=2)
    sleep(1)
    pyautogui.click(1536, 752, duration=2)
    sleep(3)

while True:
    # Abrir site instagram 'https://www.instagram.com/'
    webbrowser.open('https://www.instagram.com/')
    # Clicar e digitar login/senha
    pyautogui.click(1403, 363, duration=1)
    sleep(1)
    # Digitar Login
    pyautogui.typewrite('gabrieljlg_')
    # Precionar 'tab'
    pyautogui.press('tab')
    # Digitar Senha
    pyautogui.typewrite('dheividy789')
    sleep(1)
    # Clicar em Entrar
    pyautogui.click(1525, 473, duration=1)
    sleep(6)
    # Clicar em 'Agora não' salva senhha
    pyautogui.click(1509, 398, duration=1)
    # Clicar em 'Agora não' salva senhha
    pyautogui.click(1535, 731, duration=1)
    sleep(5)
    # Clicar em pesquisa
    pyautogui.click(1596, 152, duration=1)
    sleep(0.5)
    # Escrever Perfil que deseja 'castroraa_'
    pyautogui.typewrite('castroraa_')
    sleep(3)
    pyautogui.hotkey('down')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(5)
    # Clicar na POST mais recente
    pyautogui.click(1275, 707, duration=1)
    sleep(0.5)
    # Verificar se já foi Curtida( Se já pausar por 24h)
    coracao = pyautogui.locateCenterOnScreen("coracao.png", confidence=0.8)
    coracaob = pyautogui.locateCenterOnScreen("coracaob", confidence=0.8)
    sleep(1)
    if coracao is not None:
        logout()
        sleep(30)
    # se não curtiu curti e comentar
    elif coracaob == coracaob:
        pyautogui.click(1330, 855, duration=1)
        sleep(0.5)
        pyautogui.click(1380, 856, duration=1)
        sleep(1)
        pyautogui.click(1380, 856, duration=1)
        sleep(0.5)
        pyautogui.typewrite('linda <3')
        # Logout
        logout()
        # pausar por 24h
        sleep(30)
