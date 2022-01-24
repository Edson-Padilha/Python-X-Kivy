#coding: utf-8

#author: Edson Marciano Rodrigues Padilha

from kivy.app import App
from kivy.uix.textinput import TextInput

def build():

    return TextInput(text="Digite texto de entrada")

janela = App()
janela.build = build
janela.run()
    