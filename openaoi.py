import kivy
kivy.require('1.0.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from core import Core


class OpenAoiRoot(BoxLayout):
    """
    Root of all widgets.
    """
    def __init__(self, **kwargs):
        super(OpenAoiRoot, self).__init__(**kwargs)

    
class OpenAoi(App):
    def __init__(self, **kwargs):
        super(OpenAoi, self).__init__(**kwargs)
        
    def build(self):
        self.core = Core()
        self.core.load_options()
        
        return OpenAoiRoot()


if __name__ in ('__android__', '__main__'):
    OpenAoi().run()

