import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager

kivy.require('1.11.0')

kv = """
#:import utils kivy.utils

<ValuesGridLayout@GridLayout>:
    cols: 1
    row_default_height: 30
    size_hint_y: None
    height: self.minimum_height
    spacing: 3

<MainPanelLabel@Label>:
    text_size: self.size
    valign: "middle"
    padding_x: 5
    text: "Some content"

<MainPanel>:
    kinetic_container: kinetic_container
    thread_container: thread_container
    padding: 20, 20, 20, 0
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            ScrollView:
                GridLayout:
                    padding: [0, 10]
                    cols: 1
                    spacing: 30
                    size_hint_y: None
                    height: self.minimum_height

                    BoxLayout:
                        CheckBox:
                            size_hint: (None, None)
                            size: [20,20]
                            on_active:
                                root.toggleParameters(self.active, root.kinetic_container)

                        MainPanelLabel:
                            text: "Kinetic values:"
                            color: utils.get_color_from_hex('#f6711b')
                            font_size: '20sp'

                    ValuesGridLayout:
                        id: kinetic_container
                        visible: False
                        size: [500, 200] if self.visible else [0, 0]
                        opacity: 1 if self.visible else 0
                        disabled: not self.visible

                        MainPanelLabel
                        MainPanelLabel
                        MainPanelLabel
                        MainPanelLabel
                        MainPanelLabel
                        MainPanelLabel

                    BoxLayout:
                        CheckBox:
                            padding: 20
                            size_hint: (None, None)
                            size: [20,20]
                            on_active:
                                root.toggleParameters(self.active, root.thread_container)

                        MainPanelLabel:
                            text: "Thread values:"
                            color: utils.get_color_from_hex('#f6711b')
                            font_size: '20sp'

                    ValuesGridLayout:
                        id: thread_container
                        visible: False
                        size: [500, 200] if self.visible else [0, 0]
                        opacity: 1 if self.visible else 0
                        disabled: not self.visible

                        MainPanelLabel
                        MainPanelLabel
                        MainPanelLabel
                        MainPanelLabel
                        MainPanelLabel

<MainFrame>:
    id: screen_manager
    Screen:
        name: "Initial"
        MainPanel

"""


class MainPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(MainPanel, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.initializeSize(), 0)

    def toggleParameters(self, instance, object):
        if instance:
            object.visible = True
        else:
            object.visible = False

    def initializeSize(self):
        self.kinetic_container.size = [0, 0]
        self.thread_container.size = [0, 0]


class MainFrame(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SomeApp(App):
    def build(self):
        return MainFrame()


if __name__ == "__main__":
    Builder.load_string(kv)
    SomeApp().run()
