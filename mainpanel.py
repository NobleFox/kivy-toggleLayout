from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout


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
