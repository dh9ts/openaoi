import kivy
kivy.require('1.0.0')

# Disable multitouch-emulation
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty, StringProperty, DictProperty

import webbrowser
from core import Core


class PluginWidget(RelativeLayout):
    name = StringProperty("Plugin")
    
    #def __init__(self, **kwargs):
    #    super(PluginWidget, self).__init__(**kwargs)
    
        #settings = Button(text="S", 
        #                  pos=(20,20), 
        #                  size_hint=(None, None),
        #                  size=(30,30))
        #self.add_widget(settings)
        
class LedWidget(Widget):
    color = ListProperty([0,0,1])
    colors = DictProperty()
    status = StringProperty("")
    
    def on_status(self, instance, value):
        if value in self.colors.keys():
            self.color = self.colors[value]
        else:
            raise ValueError('Status not added to colors.')   


class OpenAoiRoot(BoxLayout):
    """
    Root of all widgets.
    """
    def __init__(self, **kwargs):
        super(OpenAoiRoot, self).__init__(**kwargs)
        # List of previous screens.
        self.screen_list = []
        
    def change_screen(self, next_screen):
        # If screen is not already in list, add it for "back-button" function.
        if self.ids.kivy_screen_manager.current not in self.screen_list:
            self.screen_list.append(self.ids.kivy_screen_manager.current)
        
        if next_screen == "about_screen":
            self.ids.kivy_screen_manager.current = "about_screen"

    def on_back_btn(self):
        if self.screen_list:
            self.ids.kivy_screen_manager.current = self.screen_list.pop()
            return True
        # No more screens to go back to. Quit app.
        return False
        
    
    
class OpenAoi(App):
    def __init__(self, **kwargs):
        super(OpenAoi, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.on_back_btn)
        
    def on_back_btn(self, window, key, *args):
        # User presses back btn
        if key == 27:
            return self.root.on_back_btn()
        
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

