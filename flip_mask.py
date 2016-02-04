# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 16:17:29 2016

@author: Geetha Yedida
"""

a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print bin(desired)