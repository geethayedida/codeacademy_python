# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:40:12 2016

@author: Geetha Yedida
"""

def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact* i
    return fact