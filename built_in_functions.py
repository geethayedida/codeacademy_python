# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:22:08 2016

@author: Geetha Yedida
"""

def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return "Nope"