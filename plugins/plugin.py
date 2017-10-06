
class PluginBase(object):
    """
    Base for all Plugins
    """
    
    STATUS_DISABLED = "disabled"
    STATUS_OK = "ok"
    STATUS_WARNING = "warning"
    STATUS_ERROR = "error"

    global_id = 0 # Unique ID for all plugin-instances.
    
    def __init__(self, config = None):
        """
        Inits a new instance of the plugins.
        If config is given, the values are loaded. Otherwise default parameters.
        """
        self.name = "PluginBase"
        self.status = self.STATUS_OK
        self.id = self.global_id
        self.global_id += 1
        
        if config is None:
            self.preferences = {"enabled": Preferences(name="enabled",
                                                       param_type=bool,
                                                       default = True)}
        else:
            pass
    
    def on_startup(self):
        """
        Called on Application startup.
        """
        pass
    
    def on_run(self):
        """
        Called to run the plugin. 
        """
        pass
    
    def on_prepare_run(self):
        """
        Called when a new run is started.
        """
        pass
    
class Preferences(object):
    """
    Class for Plugin-Preferences.
    
    Contains:
        name: Name of Parameter.
        type: Type of parameter (int, str, float, bool).
        default: Default Value if not set.
        value: Aktual value of parameter.
    """
    def __init__(self, name, param_type, default, value=None):
        self.name = name
        self.param_type = param_type
        self.default = default
        self.value = value if value is not None else default
