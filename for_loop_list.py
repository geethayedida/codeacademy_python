# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:23:54 2016

@author: Geetha Yedida
"""

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for i in start_list:
    square_list.append(i ** 2)
square_list.sort()
print square_list