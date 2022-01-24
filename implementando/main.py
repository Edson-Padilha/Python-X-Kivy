import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Tela_1(BoxLayout):

    def on_press_bt(bt):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela_2())

    
class Tela_2(BoxLayout):

    def on_press_bt(bt):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela_1())

    
class KVvsPY2(App):
    def build(self):
        return Tela_1()

janela = KVvsPY2()
janela.run()
