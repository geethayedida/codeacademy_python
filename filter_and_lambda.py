# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 12:40:26 2016

@author: Geetha Yedida
"""

squares = [x*x for x in range(1,11)]
lis = filter(lambda x : ((x  >= 30) and (x <= 70)), squares)
print lis