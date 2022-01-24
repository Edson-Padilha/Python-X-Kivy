#coding: utf-8
#author: Edson Marciano Rodrigues Padilha

from kivy.app import App
from kivy.uix.label import Label

class MeuPrograma(App):
    def build(self):
        return Label(text="Exemplo de classe")

MeuPrograma().run()