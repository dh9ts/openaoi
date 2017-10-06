import json

class Core(object):
    preferences_file = "options.json"
    
    def __init__(self):
        self.preferences = {}
        
    def save_options(self):       
        with open(self.preferences_file, 'w') as fp:
            json.dump({"preferences": self.preferences}, 
                      fp,
                      indent=4, 
                      separators=(',', ': '))
    
    def load_options(self):
        try:
            with open(self.preferences_file, 'r') as fp:
                self.preferences = json.load(fp)["preferences"]
        except IOError:
            pass
    