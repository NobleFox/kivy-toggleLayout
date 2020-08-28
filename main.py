import kivy
from kivy.app import App
from kivy.lang import Builder
from mainframe import MainFrame
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.11.0')

Builder.load_file('mainframe.kv')


class SomeApp(App):
    def build(self):
        return MainFrame()


if __name__ == "__main__":
    SomeApp().run()
