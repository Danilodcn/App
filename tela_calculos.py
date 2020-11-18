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


class TelaCalculos(BoxLayout):
    orientation = "vertical"

    def __init__(self, **kwargs):
        super(TelaCalculos, self).__init__(**kwargs)

    
    def gera_titulo(self):
        bar = ActionBar()
        view = ActionView()

        bnt_back = ActionPrevious(app_icon="./imagens/icone.png")