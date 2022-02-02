from hamcrest import none
from kivy.app import App 
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher
from kivy.lang import Builder

# Foça aplicação a não iniciar em tela cheia
from kivy.config import Config

Config.set("graphics", "fullscrean", "0")

janela = none
glayout = none 