# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:17:28 2016

@author: Geetha Yedida
"""

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)
