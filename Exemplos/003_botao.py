#coding: utf-8

#author: Edson Marciano Rodrigues Padilha

from kivy.app import App
from kivy.uix.button import Button

def click():
    print("===================")
    print("O botão foi clicado")

def build():
    bt = Button(text = "Click aqui")
    bt.on_press = click
    return bt

janela = App()
janela.build = build
janela.run()
