# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 22:39:25 2016

@author: Geetha Yedida
"""

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        print "This is a %s %s with %s MPG." %(self.model,self.color,self.mpg)

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.display_car()