import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(1015,375, duration=1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(914,312, (0, 0, 0)):
        click(914,312)
    if pyautogui.pixelMatchesColor(987,313, (0, 0, 0)):
        click(987,313)
    if pyautogui.pixelMatchesColor(1073,323, (0, 0, 0)):
        click(1073,323)
    if pyautogui.pixelMatchesColor(1131,323, (0, 0, 0)):
        click(1131,323)
