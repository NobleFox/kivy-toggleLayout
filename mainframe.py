from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import mainpanel


class MainFrame(ScreenManager):
    Builder.load_file('mainframe.kv')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
