from kivy.app import App
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

try: from .tela_home import TelaHome
except: from tela_home import TelaHome


class GerenciadorTelas(ScreenManager):
    pass


class TesteApp(App):
    
    kv_file = "kv_file.kv"
    def build(self):
        gerenciador = GerenciadorTelas()
        return gerenciador

    def on_start(self):
        home = TelaHome()
        screen = Screen(name='home')
        screen.add_widget(home)
        self.root.add_widget(screen)
        self.root.ids.update(home.ids)

        self.root.current = "home"
        print(self.root.ids)
        self.root.ids["home_botao_sair"].bind(on_release=self.home_sair)

    def home_sair(self, botao):
        box = BoxLayout(orientation="vertical", padding="10sp", spacing="10sp")
        botoes = BoxLayout(padding="10sp", spacing="10sp")

        pop = Popup(title="Quer mesmo sair?", content=box, title_size="25sp", size_hint=(.35, .35))
        pop.opacity = .85
        imagem = Image(source="./imagens/atencao.png")

        sim = Button(text="sim", font_size="20sp", on_release=App.get_running_app().stop)
        nao = Button(text="nao", font_size="20sp", on_release=pop.dismiss)
        botoes.add_widget(sim)
        botoes.add_widget(nao)

        box.add_widget(imagem)
        box.add_widget(botoes)
        pop.open()


if __name__ == "__main__":

    from kivy.core.window import Window
    Window.size = (350, 700)
    Window.clearcolor = get_color_from_hex("#4C6B8A")
    TesteApp().run()