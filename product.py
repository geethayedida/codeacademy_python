# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:46:04 2016

@author: Geetha Yedida
"""

def product(integers):
    product = 1
    for i in range(len(integers)):
        product = product * integers[i]
    return product