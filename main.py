from kivy.app import App
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

try: 
    from .tela_home import TelaHome
    from .tela_calculos import TelaCalculos
except: 
    from tela_home import TelaHome
    from tela_calculos import TelaCalculos


class GerenciadorTelas(ScreenManager):
    pass

class HomePop(Popup):
    aberto = False
    def __init__(self, **kwargs):
        super(HomePop, self).__init__(**kwargs)
        HomePop.aberto = False 

class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)

    def on_pre_enter(self):
        Window.bind(on_request_close=self.confirmacao_saida, on_keyboard=self.clica_botoes)
        Window.on_keyboard

    def clica_botoes(self, win, key, *args, **kwargs):
        if key == 27:
            self.confirmacao_saida()
        return True
        

    def confirmacao_saida(self, *args, **kw):
        if HomePop.aberto: 
            return True

        box = BoxLayout(orientation="vertical", padding="10sp", spacing="10sp")
        botoes = BoxLayout(padding="10sp", spacing="10sp")

        pop = HomePop(title="Quer mesmo sair?", content=box, title_size="20dp", size_hint=(.6, .35))
        pop.opacity = .85
        imagem = Image(source="./imagens/atencao.png")

        def fecha_popup(*args):
            HomePop.aberto = False

        pop.on_dismiss=fecha_popup

        sim = Button(text="sim", font_size="15sp", on_release=App.get_running_app().stop)
        nao = Button(text="nao", font_size="15sp", on_release=pop.dismiss)
        botoes.add_widget(sim)
        botoes.add_widget(nao)

        box.add_widget(imagem)
        box.add_widget(botoes)
 
        HomePop.aberto = True
        pop.open()
        return True


class Tela(Screen):
    def __init__(self, **kwargs):
        super(Tela, self).__init__(**kwargs)
    
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)
        

    
    def voltar(self, window, key, *args):
        print(window, key, args)
        root:ScreenManager = App.get_running_app().root
        if key == 27:
            root.current = "home"

        if root.current == "calculos":
            if key == 13 or key == 271:
                calculos = root.ids["tela_calculos"]
                calculos.faz_calculos()

        return True
    
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

class TesteApp(App):
    
    kv_file = "kv_file.kv"
    def build(self):
        gerenciador = GerenciadorTelas()
        return gerenciador

    def on_start(self):
        home = TelaHome()
        screen = Home(name='home')
        screen.add_widget(home)
        self.root.add_widget(screen)
        self.root.ids.update(home.ids)
        
        self.root.current = "home"
        self.root.ids["home_botao_sair"].bind(on_release=self.home_sair)
        self.root.ids["home_botao_calculos"].bind(on_release=self.botao_vai_para_tela("calculos"))

        self.gerar_tela_calculos()


    def home_sair(self, *args):
        home: Home = self.root.get_screen("home")
        home.confirmacao_saida()
        return True
    
    def botao_vai_para_tela(self, nome_tela:str):
        def interna(*args, **kw):
            self.root.current = nome_tela
        return interna

    def gerar_tela_calculos(self, *args):
        calculos = TelaCalculos(Window.size)
        screen = Tela(name="calculos")
        screen.add_widget(calculos)
        self.root.add_widget(screen)
        self.root.ids.update(calculos.ids)
        self.root.ids["tela_calculos"] = calculos 

        self.root.ids['calculos_botao_voltar'].bind(on_release=self.botao_vai_para_tela("home"))



if __name__ == "__main__":

    from kivy.core.window import Window
    #Window.size = (350, 700)
    Window.clearcolor = get_color_from_hex("#4C6B8A")
    TesteApp().run()