# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:20:11 2016

@author: Geetha Yedida
"""

def cube(number):
    return number ** 3
def by_three(number):
    if number % 3 == 0:
        return cube(number) 
    else:
        return False