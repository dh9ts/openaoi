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
