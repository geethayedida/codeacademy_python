# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 22:51:24 2016

@author: Geetha Yedida
"""

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        print "This is a %s %s with %s MPG." %(self.color,self.model,self.mpg)
    def drive_car(self):
        self.condition = "used"

class ElectricCar(Car):
    def __init__(self,battery_type):
        self.battery_type = battery_type
        
    def drive_car(self):
        self.condition = "like new"
        
my_car = ElectricCar("molten salt")
my_car.model = "model1"
my_car.color = "White"
my_car.mpg = 87
print my_car.condition
my_car.drive_car()
print my_car.condition