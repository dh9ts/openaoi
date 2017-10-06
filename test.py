#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 22:35:41 2017

@author: dh9ts
"""

import unittest
import os

from core import Core
from plugins.plugin import PluginBase, Preferences
from project import Project

class Util(object):
    @staticmethod
    def remove(file):
        try:
            os.remove(file)
        except:
            pass

class TestProject(unittest.TestCase):
    
    project_file = "test_project.aoi"
    
    def setUp(self):
        Util.remove(self.project_file)
               
    def tearDown(self):
        Util.remove(self.project_file)
    
    def test_save(self):
        project = self.getProject()
        project.save()
        
    def test_save_name(self):
        project = self.getProject()
        project.save(self.project_file)
        
        self.assertTrue(os.path.exists(self.project_file))
        
    def test_loading(self):
        project = self.getProject()
        project.name = "test"
        project.save(self.project_file)
        
        project2 = Project.load(self.project_file)
        self.assertEqual(project2.name, project.name)
        
    def getProject(self):
        project = Project()
        project.name = "test"
        project.file = self.project_file
        
        return project
    
    
class TestPlugin(unittest.TestCase):
    pass


class TestCorePreferences(unittest.TestCase):
    def setUp(self):
        self.core = Core()
        self.core.preferences_file = "test.json"
        
    def tearDown(self):
        Util.remove("test.json")
               
    def test_empty_class(self):
        self.assertIsNotNone(self.core.preferences)
        
    def test_store_options(self):
        self.assertNotIn("test", self.core.preferences.keys())
        
        self.core.preferences["test"] = 42
        self.core.save_options()
        
        self.core = Core()
        self.core.preferences_file = "test.json"
        self.core.load_options()
        
        self.assertIn("test", self.core.preferences.keys())
        self.assertEqual(self.core.preferences["test"], 42)
    
    def test_no_exception_if_file_not_exists(self):
        self.core.save_options()
        
        os.remove(self.core.preferences_file)
        
        self.core.load_options()
        
        self.assertIsNotNone(self.core.preferences)
        
        
class TestPreferences(unittest.TestCase):
    def setUp(self):
        self.pref = Preferences(name="nam", 
                                param_type=int, 
                                default=12, 
                                value=None)
        
    def test_name(self):
        self.assertEqual(self.pref.name, "nam")
        
    def test_type(self):
        self.assertEqual(self.pref.param_type, int)
        
    def test_default(self):
        self.assertEqual(self.pref.default, 12)
        
    def test_default_value(self):
        self.assertEqual(self.pref.value, 12)
        
        
class TestPreferencesValue(unittest.TestCase):
    def setUp(self):
        self.pref = Preferences(name="nam", 
                                param_type=int, 
                                default=12, 
                                value=13)

    def test_set_value(self):
        self.assertEqual(self.pref.value, 13)


class TestPreferencesValue2(unittest.TestCase):
    def setUp(self):
        self.pref = Preferences(name="nam", 
                                param_type=int, 
                                default=13)

    def test_set_value(self):
        self.assertEqual(self.pref.value, 13)
        

if __name__ == '__main__':
    unittest.main()
