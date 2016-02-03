# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:46:29 2016

@author: Geetha Yedida
"""

def median(ls):
    count = len(ls)
    med = sorted(ls)
    mid = count / 2
    if count  % 2 == 0:
        return (med[mid] + med[mid-1])/2.0
    else:
        return med[mid]