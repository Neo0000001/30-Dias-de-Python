import pyautogui
import webbrowser
import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.remote.webdriver import By

# Mensaje y enlace de envio al cliente
mensaje_whatsapp = """
Bienbenido al camping carlos III
"""
telefonos = ['676319076']

def envia_whasapp():
    n = 0
    for telefono in telefonos:
        webbrowser.open("https://web.whatsapp.com/send?phone="+str(telefono))
        sleep(20)
        pyautogui.typewrite(mensaje_whatsapp)
        pyautogui.press("enter")
        pyautogui.hotkey("ctrl", "w") 
        n = n + 1
