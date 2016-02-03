# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:45:35 2016

@author: Geetha Yedida
"""

def count(sequence,item):
    found = 0
    for i in range(len(sequence)):
        if item == sequence[i]:
            found = found + 1
    return found 