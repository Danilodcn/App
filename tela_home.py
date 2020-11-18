from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious, ActionButton, ActionLabel, ActionSeparator
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex
from kivy.metrics import sp

import os, random

class TelaHome(BoxLayout):
    
    def __init__(self, **kwargs):
        super(TelaHome, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.KEY = 0
        self.gera_imagem()
        self.gera_botoes(.3)

    def botao(self, botao):

        dirs = os.listdir("./imagens/home")
        fonte = random.choice(dirs)
        fonte = "./imagens/home/" + fonte

        self.ids["imagem_home"].source = fonte

    def gera_imagem(self):
        box = BoxLayout(padding='10sp', spacing="20sp")
        dirs = os.listdir("./imagens/home")
        fonte = random.choice(dirs)
        fonte = "./imagens/home/" + fonte
        imagem = Image(source=fonte)
        box.add_widget(imagem)
        self.ids["imagem_home"] = imagem
        self.add_widget(box)

    def gera_botoes(self, h_rint=1):
        p = [f"{i}sp" for i in [40, 5, 40, 40]]
        box = BoxLayout(orientation="vertical", padding=p, spacing="10sp")
        box.size_hint_y = h_rint
        
        bnt0 = Button(text="Atualizar", on_release=self.botao)
        bnt1 = Button(text="Calculos")
        bnt2 = Button(text="Sair")
        
        box.add_widget(bnt0)
        box.add_widget(bnt1)
        box.add_widget(bnt2)
        self.add_widget(box)
        self.ids["home_botao_calculos"] = bnt1
        self.ids["home_botao_sair"] = bnt2
        