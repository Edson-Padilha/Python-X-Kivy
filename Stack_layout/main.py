import kivy
kivy.require("1.9.1")
from kivy.interactive import InteractiveLauncher
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.lang import Builder

from kivy.config import Config
Config.set("graphics","fullscreen","0")#Define que não inicie em tela cheia

janela = None
glayout = None

class EstudoStackLayoutApp(App):
    pass

janela = EstudoStackLayoutApp()
janela.run()

if (janela.root):
    janela.root_window.remove_widget(janela.root)
    janela.root = None
    glayout = None

janela.root = glayout = Builder.load_string(Kvcode)
janela.root_window.add_widget(glayout)
#glayout.add_widget(Button(text="Z", size_hint=(.33,.1))) Cria novo botão