# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 20:03:36 2016

@author: Geetha Yedida
"""

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age
    
hippo = Animal("Hippopotamus", 98)
hippo.description()