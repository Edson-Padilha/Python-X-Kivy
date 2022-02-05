
import kivy
kivy.require("1.9.1")
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.interactive import InteractiveLauncher
from kivy.lang import Builder

from kivy.config import Config
Config.set("graphics", "fullscreen", "0")#Define que não inicia em tela cheia

janela = None
glayout = None

class EstudoBoxLayoutApp(App):
    pass

janela = EstudoBoxLayoutApp()
janela.run()

if(janela.root):
    janela.root_window.remove_widget(janela.root)
    janela.root = None
    glayout = None

janela.root = glayout = Builder.load_string(Kvcode)
janela.root_window.add_widget(glayout)
