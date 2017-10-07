# -*- coding: utf-8 -*-

import json

from project import Project


class Core(object):
    preferences_file = "options.json"
    
    def __init__(self):
        self.preferences = {}
        self.project = Project()
        
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
        
    def getConfigValue(self, name, default=None):
        value = self.preferences.get(name, default)
        
        names = name.split(".")
        stage = self.preferences
        
        for index, name in enumerate(names):
            if index == len(names) - 1:
                value = stage.get(name, default)
                
            stage = stage.get(name, {})
        
        return value
    
    def setConfigValue(self, name, value):
        names = name.split(".")
        stage = self.preferences
        
        for index, name in enumerate(names):
            if index == len(names) - 1:
                stage[name] = value

            if name not in stage.keys():
                stage[name] = {}
            
            stage = stage[name]
            
    def _dump_options(self):
        return json.dumps({"preferences": self.preferences}, 
                          indent=4, 
                          separators=(',', ': '))
        
