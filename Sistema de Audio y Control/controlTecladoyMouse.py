import pyautogui as controlTecladoyMouse
import subprocess
import os


def buscar(texto):
    subprocess.call(
        ['google-chrome', 'www.google.com/search?q={0}'.format(texto)])


def cerrarVentana():
    controlTecladoyMouse.hotkey('alt', 'f4')

  
def scrollDown():
    controlTecladoyMouse.scroll(-10)
    # controlTecladoyMouse.press('j')


def scrollUp():
    controlTecladoyMouse.scroll(10)
    # controlTecladoyMouse.press('k')


def acercar():
    controlTecladoyMouse.hotkey('ctrl', '+')


def alejar():
    controlTecladoyMouse.hotkey('ctrl', '-')


def nuevo():
    controlTecladoyMouse.hotkey('ctrl', 'n')

def foto():
    controlTecladoyMouse.hotkey('ctrl', 'p')

def enter():
    controlTecladoyMouse.hotkey('enter')

def siguienteChat():
    controlTecladoyMouse.hotkey('ctrl', 'tab')

def buscarChat():
    controlTecladoyMouse.hotkey('ctrl', 'f')

def anteriorChat():
    controlTecladoyMouse.hotkey('ctrl', 'shift', 'tab')


def escribir(texto):
    texto = replace(texto)
    controlTecladoyMouse.typewrite(texto)


def minimizar():
    controlTecladoyMouse.hotkey('win', 'm')


def restaurar():
    controlTecladoyMouse.hotkey('win', 'shift', 'm')

def abrir():   
    os.system('WhatsApp.exe')

def abrir1():
    os.system('WhatsApp.exe')


def escape():
    controlTecladoyMouse.press('esc')

def borrar():
    controlTecladoyMouse.hotkey('ctrl', 'backspace')

def borrarTexto():
    controlTecladoyMouse.hotkey('backspace')

def borrarTodo():
    controlTecladoyMouse.hotkey('ctrl', 'a')    
    controlTecladoyMouse.hotkey('backspace')


def replace(texto):
    texto.replace("á","a")
    texto.replace("é","e")
    texto.replace("í","i")
    texto.replace("ó","o")
    texto.replace("ú","u")
    return texto