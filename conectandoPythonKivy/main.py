import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MinhaTela(BoxLayout):

    def click(self):
        print("Oi!")
        self.ids.lb1.text = "Trocou o nome!!!"
        self.ids.lb2.text = "Parabéns!!!"

class Estudo4App(App):
    pass

janela = Estudo4App()
janela.run()