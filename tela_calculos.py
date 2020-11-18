from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious, ActionButton, ActionLabel, ActionSeparator
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex
from kivy.metrics import sp


class TelaCalculos(BoxLayout):
    orientation = "vertical"

    def __init__(self, size,  **kwargs):
        super(TelaCalculos, self).__init__(**kwargs)
        self.gera_titulo()
        self.gera_ler_dados()
        self.size = size

    def gera_ler_dados(self):
        box_geral = BoxLayout(orientation="vertical")

        spacing = "20sp"
        padding = [f"{i}sp" for i in [10, 50, 10, 50]]

        grid = GridLayout(cols=2, size_hint_y=None, spacing=spacing, padding=padding)
        grid.bind(minimum_height=grid.setter("height"))

        nomes = "Peso_em_Arrobas Preco_em_Arrobas Peso_em_KG Preco_em_Reais"
        nomes = nomes.split()
        altura = sp(30)
        for nome in nomes:
            txt = " ".join(nome.split("_"))
            lb = Label(text=txt, size_hint_y=None, height=altura)

            inp = TextInput(write_tab=False, input_filter="float", multiline=False)
            grid.add_widget(lb)
            grid.add_widget(inp)
            self.ids["calculos_input_" + nome.lower()] = inp


        scroll = ScrollView(size_hint=(1, 1))
        #scroll.width = self.width * .9
        #scroll.height = self.height * .85
        #scroll.add_widget(grid)

        #box_geral.add_widget(scroll)
        
        bnt = Button(text="Relizar os Calculos", size_hint_y=None, height="30sp")
        bnt.on_release = self.faz_calculos
        self.ids["calculos_botao_calculos"] = bnt
        p = [f"{i}sp" for i in [40, 0, 40, 40]]
        box = BoxLayout(orientation="vertical", padding=p)
        box.add_widget(bnt)
        box_geral.add_widget(grid)
        box_geral.add_widget(box)
        scroll.add_widget(box_geral)
        self.add_widget(scroll)
        

    
    def gera_titulo(self):
        bar = ActionBar()
        view = ActionView()

        bnt_back = ActionPrevious(app_icon="./imagens/icone.png")
        bnt_back.size_hint = (.9, .9)
        bnt_back.title = "Cálculos"

        view.add_widget(bnt_back)
        bar.add_widget(view)
        
        self.add_widget(bar)
        self.ids["calculos_botao_voltar"] = bnt_back


    def faz_calculos(self, *args):
        dados = []
        logs = []
        for key in self.ids.keys():
            if "input" in key:
                inp = self.ids[key]
                try: dados.append(float(inp.text))
                except: 
                    dados.append(0)
                    #logs.append('O numero em "{}" nao é inteiro'.format(" ".join(key.split("_")[2:]).upper()) )
        print(dados)
        if logs:
            print(logs)
        else:
            dados = self._calcula(dados)
            dados = [round(valor, 3) for valor in dados]
            i = 0
            for key in self.ids.keys():
                if "input" in key:
                    inp = self.ids[key]
                    txt = "" if dados[i] == 0 else dados[i]
                    inp.text = str(txt)
                    i += 1
            
    
    
    def _calcula(self, dados):
        peso_arrobas, preco_arrobas, peso_kg, preco = dados
        if peso_arrobas > 0:
            peso_kg = peso_arrobas * 30
            if preco_arrobas > 0:
                preco = preco_arrobas * peso_arrobas

            elif preco > 0:
                preco_arrobas = preco / peso_arrobas

        elif peso_kg > 0:
            peso_arrobas = peso_kg / 30
            if preco_arrobas > 0:
                preco = preco_arrobas * peso_arrobas

            elif preco > 0:
                preco_arrobas = preco / peso_arrobas

        return peso_arrobas, preco_arrobas, peso_kg, preco

if __name__ == "__main__":
    dados = [0, 10, 30, 0]
    peso_arrobas, preco_arrobas, peso_kg, preco = dados
    x = TelaCalculos((2, 4))
    y = x._calcula(dados)
    print(y)