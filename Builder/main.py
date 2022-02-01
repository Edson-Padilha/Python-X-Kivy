
import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


code = """
BoxLayout:
    Button:
        text:"1"

    Button:
        text:"2"
"""
from kivy.lang import Builder
#Builder.load_file(code)

class Estudo6App(App):
    def buider(self):
        return Builder.load_string(code)

janela = Estudo6App()
janela.run()