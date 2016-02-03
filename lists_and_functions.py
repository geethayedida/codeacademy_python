# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:25:27 2016

@author: Geetha Yedida
"""

# Write your function below!
def fizz_count(x):
    count = 0
    for i in x:
        if i == "fizz":
            count = count + 1
    return count