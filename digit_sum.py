# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:40:26 2016

@author: Geetha Yedida
"""

def digit_sum(n):
    sum = 0
    n = str(n)
    for i in n:
        sum = sum + int(i)
    return sum