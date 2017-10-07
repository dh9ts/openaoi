import kivy
kivy.require('1.0.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

import webbrowser
from core import Core


class OpenAoiRoot(BoxLayout):
    """
    Root of all widgets.
    """
    def __init__(self, **kwargs):
        super(OpenAoiRoot, self).__init__(**kwargs)
        
    def change_screen(self, next_screen):
        if next_screen == "about_screen":
            self.ids.kivy_screen_manager.current = "about_screen"

    
class OpenAoi(App):
    def __init__(self, **kwargs):
        super(OpenAoi, self).__init__(**kwargs)
        
    def build(self):
        self.core = Core()
        self.core.load_options()
        
        root = OpenAoiRoot()
        
        Window.size = self.core.getConfigValue("gui.window.size", (800, 600))
        pos = self.core.getConfigValue("gui.window.position", (100, 100))
        #Window.left = pos[0]
        #Window.top = pos[1]
        
        return root
    
    def on_stop(self):
        # Store size and position.
        self.core.setConfigValue("gui.window.size", Window.size)
        # Storing of position is not working at the moment!
        pos = (Window.left, Window.top)
        self.core.setConfigValue("gui.window.position", pos)
        
        self.core.save_options()
        
    def getText(self):
        return ("OpenAOI. This App was build using [b][ref=kivy]Kivy[/ref][/b]\n"
               "The source is hosted on [b][ref=git]Github[/ref][/b].")
        
    def on_ref_press(self, instace, ref):
        _dict = {
                    "kivy": "http://kivy.org",
                    "git": "https://github.com/dh9ts/openaoi"
                }
        webbrowser.open(_dict[ref])


if __name__ in ('__android__', '__main__'):
    OpenAoi().run()

