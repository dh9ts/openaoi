# -*- coding: utf-8 -*-
import jsonpickle

class Project(object):
    """ Base class for a project."""
    def __init__(self):
        self.steps = []
        self.name = "untitled"
        self.file = self.name + ".aoi"
        
        jsonpickle.set_encoder_options('simplejson', 
                                       sort_keys=True, 
                                       indent=4)
    
    def save(self, filename=None):
        if filename is not None:
            self.file = filename
         
        data = jsonpickle.encode(self)
        
        with open(self.file, 'w') as fp:
            fp.write(data)
     
    @staticmethod
    def load(filename):
        with open(filename, 'r') as fp:
            return jsonpickle.decode(fp.read())