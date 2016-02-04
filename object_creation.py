# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 19:45:33 2016

@author: Geetha Yedida
"""

class Animal(object):
    def __init__(self, name):
        self.name = name

zebra = Animal("Jeffrey")
print zebra.name