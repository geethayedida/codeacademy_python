# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:39:59 2016

@author: Geetha Yedida
"""

def is_prime(x):   
    if x<2:
        return False
    elif x==2:
        return True
    for i in range(2,x-1):
        if x % i == 0:
            return False
            break
    else:
        return True