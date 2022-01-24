#coding: utf-8
#author: Edson Marciano Rodrigues Padilha

import kivy
kivy.require('1.9.1') #menor versão a ser executada

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Tela_1(BoxLayout):

    def on_press_bt(bt):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela_2())

    def __init__(self, **kwargs):
        super(Tela_1, self).__init__(**kwargs)
        self.orientation = "vertical"
        bt1 = Button(text="btn1")
        bt1.on_press = self.on_press_bt
        self.add_widget(bt1)
        self.add_widget(Button(text="btn2"))
        self.add_widget(Button(text="btn3"))

class Tela_2(BoxLayout):
    
    
    def on_press_bt(bt):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela_1())

    def __init__(self, **kwargs):
        super(Tela_2, self).__init__(**kwargs)
        self.orientation = "vertical"
        bt10 = Button(text="btn10")
        bt10.on_press = self.on_press_bt
        self.add_widget(bt10)

class KVvsPY(App):
    def build(self):
        return Tela_1()

janela = KVvsPY()
janela.run()