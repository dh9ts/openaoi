#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 22:35:41 2017

@author: dh9ts
"""

import unittest
from plugins.plugin import PluginBase, Preferences

class TestPlugin(unittest.TestCase):
    pass


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
