# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 21:00:01 2016

@author: Geetha Yedida
"""

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age
    
hippo = Animal("Hippopotamus", 98)
sloth = Animal("Sloth",3)
ocelot = Animal("Ocelot", 2)
hippo.description()
print hippo.health
print sloth.health
print ocelot.health