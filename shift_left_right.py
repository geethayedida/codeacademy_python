# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 15:09:19 2016

@author: Geetha Yedida
"""

shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2
print bin(shift_right)
print bin(shift_left)