from main import TesteApp
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.size = (350, 700)
Window.clearcolor = get_color_from_hex("#4C6B8A")

TesteApp().run()

