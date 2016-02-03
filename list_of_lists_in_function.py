# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:32:20 2016

@author: Geetha Yedida
"""

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
    results = []
    for number in lists:
        results = results + number
    return results


print flatten(n)