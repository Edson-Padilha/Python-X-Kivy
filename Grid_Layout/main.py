import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.interactive import InteractiveLauncher

from kivy.config import Config

Config.set("graphics", "fullscreen", "1")
janela = None
glayout = None

class EstudoGridLayoutApp(App):
    pass

janela = EstudoGridLayoutApp()
janela.run()